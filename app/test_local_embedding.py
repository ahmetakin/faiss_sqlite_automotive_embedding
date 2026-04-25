import os
#Offline mod ve GPU ayarları
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_DATASETS_OFFLINE"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "2,3"

from transformers import AutoProcessor, AutoModel
from PIL import Image
import torch
import numpy as np

#model ve örnek resim path
MODEL_PATH = "/home/user/ahmet-ai/qwen3.59bserver/local_multimodal_lab/data/faiss_sqlite/model/Qwen3-VL-Embedding-2B"
IMAGE_PATH = "/home/user/ahmet-ai/qwen3.59bserver/local_multimodal_lab/data/faiss_sqlite/app/car_battery.jpeg"

# vektördeki değerlerin karelerinin toplamının karekökünü (Öklid mesafesi) kullanarak veriyi normalize ederiz
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

#metinleri embedding’e çeviriyor.
#query ve document ayrım önemli. Çünkü embedding modellerinde query ve document farklı prompt ile verilirse retrieval kalitesi artabilir.
def encode_text(model, processor, texts, mode="document"):
    if mode == "query":
        prepared_texts = [
            f"Represent this query for retrieving relevant documents: {text}"
            for text in texts
        ]
    elif mode == "document":#Dokümanları vektörleştirirken kullanılıyor.
        prepared_texts = [
            f"Represent this document for retrieval: {text}"
            for text in texts
        ]
    else:
        prepared_texts = texts

    #metni token haline getiriyor.
    inputs = processor(
        text=prepared_texts,
        return_tensors="pt",
        padding=True,
        truncation=True
    )

    inputs = move_inputs_to_device(inputs, model.device)

    with torch.no_grad():
        outputs = model(**inputs) #modelden embedding çıkarıyor.

    embeddings = get_embedding_from_outputs(outputs, inputs)
    embeddings = embeddings.float().cpu().numpy()
    embeddings = l2_normalize(embeddings) # normalize edip geri döndürüyor.

    return embeddings

#Bu fonksiyon görseli embedding’e çeviriyor.
def encode_image(model, processor, image_paths):
    images = []

    for image_path in image_paths:
        #Görsel açılıyor, RGB’ye çevriliyor ve maksimum 448x448 boyutuna küçültülüyor.
        image = Image.open(image_path).convert("RGB")
        image.thumbnail((448, 448))
        images.append(image)
    #Sonra modelin beklediği görsel token alınıyor:
    image_token = getattr(processor, "image_token", "<|image_pad|>")

    #modele “bu görseli retrieval için temsil et” deniyor.
    image_prompts = [
        f"Represent this image for retrieval: {image_token}"
        for _ in images
    ]

    #Sonra metin + görsel birlikte processor’dan geçirilip embedding üretiliyor.
    inputs = processor(
        text=image_prompts,
        images=images,
        return_tensors="pt",
        padding=True
    )

    inputs = move_inputs_to_device(inputs, model.device)

    with torch.no_grad():
        outputs = model(**inputs)

    embeddings = get_embedding_from_outputs(outputs, inputs)
    embeddings = embeddings.float().cpu().numpy()
    embeddings = l2_normalize(embeddings)

    return embeddings

#İki embedding kümesi arasında benzerlik hesaplıyor.
#Skor 1’e ne kadar yakınsa benzerlik o kadar yüksek.
def cosine_similarity(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.matmul(a, b.T)


def main():
    #PyTorch sürümünü, CUDA var mı, kaç GPU görüyor bunları yazdırıyor.
    print("Torch:", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())
    print("CUDA device count:", torch.cuda.device_count())

    #Processor; metinleri tokenize eder, görselleri modele uygun tensora çevirir.
    processor = AutoProcessor.from_pretrained(
        MODEL_PATH,
        local_files_only=True,
        trust_remote_code=True
    )
    #Model lokal klasörden yükleniyor.
    model = AutoModel.from_pretrained(
        MODEL_PATH,
        local_files_only=True,#İnternete çıkma.
        trust_remote_code=True,#Modelin özel Python kodlarını kullanmasına izin ver.
        dtype=torch.float16,#Modeli FP16 yükle, VRAM daha az kullanılsın.
        device_map="auto",#Modeli GPU’lara otomatik dağıt.
        low_cpu_mem_usage=True#Yükleme sırasında CPU RAM kullanımını azalt.
    )

    model.eval()

    print("Model device:", model.device)
    #Bunlar küçük bir örnek veri tabanı gibi düşünülüyor.
    documents = [
        "Otomotiv servisinde fren balataları kontrol edilir.",
        "Elektrikli araç bataryası garanti süresi 8 yıldır.",
        "Yedek parça deposunda stok kartı açılmalıdır.",
        "Bugün hava çok güneşli ve parkta yürüyüş yapmak güzel olur.",
        "Python ile FAISS kullanarak vektör arama yapılabilir."
    ]
    #Bu normal metin arama sorgusu.
    query = "elektrikli araç batarya garanti süresi"
    #Bu ise görsele daha yakın kavramlarla yazılmış metinsel sorgu.
    #Yani görselde araba aküsü varsa, bu sorgunun görsel embeddingine daha yakın çıkması beklenir.
    visual_query = "araba aküsü elektrikli araç bataryası otomotiv batarya"

    #5 doküman embedding’e çevriliyor.
    #5 doküman var, her biri 2048 boyutlu vektör.
    document_embeddings = encode_text(
        model=model,
        processor=processor,
        texts=documents,
        mode="document"
    )
    #Arama cümlesi embedding’e çevriliyor.
    query_embedding = encode_text(
        model=model,
        processor=processor,
        texts=[query],
        mode="query"
    )
    #Görseli temsil eden metinsel sorgu embedding’e çevriliyor.
    visual_query_embedding = encode_text(
        model=model,
        processor=processor,
        texts=[visual_query],
        mode="query"
    )

    print("\nDocument embeddings shape:", document_embeddings.shape)
    print("Query embedding shape:", query_embedding.shape)
    print("Visual query embedding shape:", visual_query_embedding.shape)
    print("İlk document embedding ilk 8 değer:", document_embeddings[0][:8])

    #Burada query ile tüm dokümanlar karşılaştırılıyor.
    text_scores = cosine_similarity(query_embedding, document_embeddings)[0]

    print("\nText query - text document arama sonuçları:")
    #skorları büyükten küçüğe sıralıyor.
    for idx in np.argsort(text_scores)[::-1]:
        print(f"Skor: {text_scores[idx]:.4f} | Metin: {documents[idx]}")

    #“araba aküsü elektrikli araç bataryası...” sorgusuyla dokümanlar aranıyor.
    visual_text_scores = cosine_similarity(visual_query_embedding, document_embeddings)[0]

    
    print("\nVisual query - text document arama sonuçları:")
    for idx in np.argsort(visual_text_scores)[::-1]:
        print(f"Skor: {visual_text_scores[idx]:.4f} | Metin: {documents[idx]}")

    if os.path.exists(IMAGE_PATH):
        #Görsel embedding’e çevriliyor.
        image_embeddings = encode_image(
            model=model,
            processor=processor,
            image_paths=[IMAGE_PATH]
        )

        print("\nImage embedding shape:", image_embeddings.shape)
        print("İlk image embedding ilk 8 değer:", image_embeddings[0][:8])

        #“Elektrikli araç batarya garanti süresi” sorgusu ile bu görsel birbirine ne kadar benziyor?
        #Eğer görsel araba aküsü/batarya ise skor makul yüksek çıkabilir.
        image_score_with_text_query = cosine_similarity(
            query_embedding,
            image_embeddings
        )[0][0]

        #Burada şu soruluyor:“Araba aküsü elektrikli araç bataryası otomotiv batarya” metni ile görsel birbirine ne kadar benziyor?
        #Bu skorun genelde daha yüksek çıkması beklenir çünkü visual query görselin içeriğini daha doğrudan tarif ediyor.
        image_score_with_visual_query = cosine_similarity(
            visual_query_embedding,
            image_embeddings
        )[0][0]

        print("\nText query - image similarity:")
        print(f"Skor: {image_score_with_text_query:.4f} | Query: {query}")

        print("\nVisual query - image similarity:")
        print(f"Skor: {image_score_with_visual_query:.4f} | Query: {visual_query}")

        print(f"\nGörsel: {IMAGE_PATH}")

    else:
        print(f"\nGörsel bulunamadı: {IMAGE_PATH}")


if __name__ == "__main__":
    main()


#Bu kod küçük bir multimodal semantic search testi yapıyor.
#1 Lokal Qwen3-VL-Embedding-2B modelini yüklüyor.
#2 Metin dokümanlarını embedding’e çeviriyor.
#3 Metinsel sorguyu embedding’e çeviriyor.
#4 Görsel açıklaması gibi bir sorguyu embedding’e çeviriyor.
#5 Varsa görseli embedding’e çeviriyor.
#6 Metin-metin benzerliği hesaplıyor.
#7 Metin-görsel benzerliği hesaplıyor.
#8 Sonuçları cosine similarity skoruna göre yazdırıyor.


'''
Öncelikle kullandığın model daha önceden görselle ve metinler ile eğitildiği için neyi nasıl çevireceğini bilir
1-Misal araba aküsü görselini daha önceden captionu ile öğrendiği için ona göre temsili öğretir bu sebepten burada sorgulatığımızda ona göre getirecektir
2-Fakat tc li şahsın resmini getir gibi bir sorgu attığımızda eğitim verisinde bu resim daha önceden olmadığı için metadata verisinden faydalanır
3-burada 
    Represent this image for retrieval:
    Represent this query for retrieving relevant documents:
    Represent this document for retrieval:
    gibi eklemeler hangi şeyi ne amacla vektöre çevireceğini söylüyoruz.
4-query ve visual_query ise aradığımız şeye yakın değerleri bulması için var
5-resimden kişiyi kim olduğunu bilmez embedding model sadece """insan", "erkek", "kadın", "gülüyor", "yaşlı""" gibi bilgileri bilir misal, kişiyi bilmesi için kimlik bilgilerini metadata eklemen gerekir
6-misal resim atıp bu kişiye benzer kişiyi getir dersen embedding üzerinden arama yapar metadata dan kişinin bilgilerini alır gerekirse mcp ile istenilen ek verileri getirebilir.
7-"TC 12345678901 olan kişiyi getir" gibi bir çıkarım yapamaz fakat tabiki bu sorgu sql olarak mcp aracılığı ile gidebilir
8-görseller bilgiğin gibi "Resim → patch'lere böl → transformer → embedding" embeddingleri oluşur
9-
'''