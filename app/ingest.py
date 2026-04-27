import json
from pathlib import Path

import numpy as np

from app.config import RAW_DOCUMENTS_PATH, DATA_DIR
from app.db import clear_db, insert_item
from app.embedder import QwenVLEmbedder
from app.index_store import FaissIndexStore


def build_text_for_embedding(item: dict) -> str:
    """
    Sadece content'i değil, başlık/kategori/ürün kodu gibi aramada faydalı alanları da
    embedding metnine ekliyoruz.
    """
    parts = [
        f"Başlık: {item.get('title', '')}",
        f"Kategori: {item.get('category', '')}",
        f"Ürün kodu: {item.get('product_code', '')}",
        f"Kaynak: {item.get('source', '')}",
        f"İçerik: {item.get('content', '')}"
    ]

    metadata = item.get("metadata") or {}
    if metadata:
        metadata_text = " ".join([f"{k}: {v}" for k, v in metadata.items()])
        parts.append(f"Metadata: {metadata_text}")

    return "\n".join(parts)


def resolve_image_path(relative_path: str | None):
    if not relative_path:
        return None

    return str(DATA_DIR / relative_path)


def ingest_all():
    with open(RAW_DOCUMENTS_PATH, "r", encoding="utf-8") as f:
        items = json.load(f)

    clear_db()

    embedder = QwenVLEmbedder()

    all_embeddings = []
    vector_ids = []

    vector_id_counter = 1

    for item in items:
        item_type = item["type"]

        if item_type == "text":
            embedding_text = build_text_for_embedding(item)

            embedding = embedder.encode_texts(
                [embedding_text],
                mode="document"
            )[0]

        elif item_type == "image":
            image_path = resolve_image_path(item.get("image_path"))

            if image_path is None or not Path(image_path).exists():
                print(f"Görsel bulunamadı, atlanıyor: {image_path}")
                continue

            embedding = embedder.encode_images([image_path])[0]

        else:
            print(f"Bilinmeyen item type, atlanıyor: {item_type}")
            continue

        vector_id = vector_id_counter
        vector_id_counter += 1

        insert_item(
            vector_id=vector_id,
            item_id=item["item_id"],
            item_type=item["type"],
            title=item["title"],
            category=item.get("category"),
            product_code=item.get("product_code"),
            source=item.get("source"),
            content=item.get("content"),
            image_path=item.get("image_path"),
            metadata=item.get("metadata") or {}
        )

        all_embeddings.append(embedding)
        vector_ids.append(vector_id)

        print(f"Eklendi: vector_id={vector_id} | {item['item_id']} | {item['title']}")

    if not all_embeddings:
        raise RuntimeError("Hiç embedding üretilemedi.")

    embeddings_matrix = np.vstack(all_embeddings).astype("float32")

    index_store = FaissIndexStore()
    index_store.build(embeddings_matrix, vector_ids)
    index_store.save()

    print("\nIngestion tamamlandı.") #veriyi yükleme
    print("Toplam kayıt:", len(vector_ids))
    print("Embedding shape:", embeddings_matrix.shape)

#Burada Captione text embedding bulunmuyor şuan görseller için vektörize ettiğimiz 2. aşamada denenecek
#Ekledikten sonra görsel benzerlik ve açıklama benzerliği güçlenecek
#