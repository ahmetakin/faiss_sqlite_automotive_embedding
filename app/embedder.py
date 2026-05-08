#verileri embed edecek olan kod resim ve text verilerini vektörize ediceğiz

import os

os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_DATASETS_OFFLINE"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "2,3"
from tqdm import tqdm
from typing import List
import numpy as np
import torch
from PIL import Image
from transformers import AutoProcessor, AutoModel

from app.config import MODEL_PATH, IMAGE_MAX_SIZE

# vektördeki değerlerin karelerinin toplamının karekökünü (Öklid mesafesi) kullanarak veriyi normalize ederiz
#vektör hazırlıgı 1 birime eşitler tüm cümlelerin büyüklüğünü değil, sadece yönünü anlamını önemsememizi sağlar
def l2_normalize(x: np.ndarray) -> np.ndarray:
    norm = np.linalg.norm(x, axis=1, keepdims=True)
    return x / np.clip(norm, 1e-12, None)

#verileri gpu'ya taşır
def move_inputs_to_device(inputs, device):
    return {
        k: v.to(device) if torch.is_tensor(v) else v
        for k, v in inputs.items()
    }

#attention mask’e göre ortalayıp tek bir vektör yaparız.
def mean_pooling(last_hidden_state, attention_mask):
    mask = attention_mask.unsqueeze(-1).expand(last_hidden_state.size()).float()
    summed = torch.sum(last_hidden_state * mask, dim=1)
    counts = torch.clamp(mask.sum(dim=1), min=1e-9)
    return summed / counts

#model hangi formatta embedding verirse versin, onu yakalamaya çalışıyor.
def get_embedding_from_outputs(outputs, inputs=None):
    if hasattr(outputs, "embeddings") and outputs.embeddings is not None:
        emb = outputs.embeddings

    elif hasattr(outputs, "sentence_embedding") and outputs.sentence_embedding is not None:
        emb = outputs.sentence_embedding

    elif hasattr(outputs, "pooler_output") and outputs.pooler_output is not None:
        emb = outputs.pooler_output

    elif hasattr(outputs, "last_hidden_state") and outputs.last_hidden_state is not None:
        if inputs is not None and "attention_mask" in inputs:
            emb = mean_pooling(outputs.last_hidden_state, inputs["attention_mask"])
        else:
            emb = outputs.last_hidden_state.mean(dim=1)

    else:
        available = outputs.keys() if hasattr(outputs, "keys") else outputs
        raise RuntimeError(f"Embedding çıktısı bulunamadı. Output alanları: {available}")

    return emb


class QwenVLEmbedder:
    def __init__(self):
        print("Embedding modeli yükleniyor...")

        self.processor = AutoProcessor.from_pretrained(
            MODEL_PATH,
            local_files_only=True,
            trust_remote_code=True
        )

        self.model = AutoModel.from_pretrained(
            MODEL_PATH,
            local_files_only=True,
            trust_remote_code=True,
            dtype=torch.float16,
            device_map="auto",
            low_cpu_mem_usage=True
        )

        self.model.eval()

        print("Model hazır.")
        print("Model device:", self.model.device)

    #metinleri embedding’e çeviriyor.
    #query ve document ayrım önemli. Çünkü embedding modellerinde query ve document farklı prompt ile verilirse retrieval kalitesi artabilir.
    def encode_texts(self, texts: List[str], mode: str = "document", batch_size: int = 32) -> np.ndarray:
        all_embeddings = []

        # Listeyi parçalara (batch) bölüyoruz
        for i in tqdm(range(0, len(texts), batch_size), desc="Metinler işleniyor"):
            batch_texts = texts[i : i + batch_size]
            
            if mode == "query":
                prepared_texts = [f"Represent this query for retrieving relevant documents: {text}" for text in batch_texts]
            elif mode == "document":
                prepared_texts = [f"Represent this document for retrieval: {text}" for text in batch_texts]
            else:
                prepared_texts = batch_texts

            inputs = self.processor(
                text=prepared_texts,
                return_tensors="pt",
                padding=True,
                truncation=True
            )

            inputs = move_inputs_to_device(inputs, self.model.device)

            with torch.no_grad():
                outputs = self.model(**inputs)

            batch_emb = get_embedding_from_outputs(outputs, inputs)
            batch_emb = batch_emb.float().cpu().numpy()
            all_embeddings.append(batch_emb)
            
            # Belleği temizlemek için (opsiyonel ama önerilir)
            del outputs, inputs, batch_emb
            torch.cuda.empty_cache()

        # Tüm parçaları birleştir ve normalize et
        embeddings = np.vstack(all_embeddings)
        embeddings = l2_normalize(embeddings)

        return embeddings.astype("float32")


    #Bu fonksiyon görseli embedding’e çeviriyor.
    def encode_images(self, image_paths: List[str], batch_size: int = 8) -> np.ndarray:
        all_embeddings = []
        image_token = getattr(self.processor, "image_token", "<|image_pad|>")

        # Listeyi batch_size büyüklüğünde parçalara bölüyoruz
        for i in tqdm(range(0, len(image_paths), batch_size), desc="Resimler işleniyor"):
            batch_paths = image_paths[i : i + batch_size]
            batch_images = []

            # Sadece mevcut batch'teki resimleri yükle ve işle
            for path in batch_paths:
                image = Image.open(path).convert("RGB")
                image.thumbnail((IMAGE_MAX_SIZE, IMAGE_MAX_SIZE))
                batch_images.append(image)

            image_prompts = [
                f"Represent this image for retrieval: {image_token}"
                for _ in batch_images
            ]

            # Processor ile batch'i hazırla
            inputs = self.processor(
                text=image_prompts,
                images=batch_images,
                return_tensors="pt",
                padding=True
            )

            inputs = move_inputs_to_device(inputs, self.model.device)

            with torch.no_grad():
                outputs = self.model(**inputs)

            # Embedding'leri al ve CPU'ya çek
            batch_emb = get_embedding_from_outputs(outputs, inputs)
            batch_emb = batch_emb.float().cpu().numpy()
            all_embeddings.append(batch_emb)

            # Bellek temizliği
            del outputs, inputs, batch_images, image_prompts
            torch.cuda.empty_cache()

        # Tüm batch'leri dikey olarak birleştir
        embeddings = np.vstack(all_embeddings)
        # L2 Normalizasyonu tüm listeye uygula
        embeddings = l2_normalize(embeddings)

        return embeddings.astype("float32")



#Metin ve Görsel embedding'leri aynı normalize edilmiş uzaya konulur
#Böylece Faiss tek index ile hem text-totext hem text-to-image arama yapılabilir