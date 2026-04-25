from app.db import fetch_item_by_vector_id
from app.embedder import QwenVLEmbedder
from app.index_store import FaissIndexStore
from app.config import TOP_K


def search_by_text(query: str, top_k: int = TOP_K):
    embedder = QwenVLEmbedder()

    query_embedding = embedder.encode_texts(
        [query],
        mode="query"
    )

    index_store = FaissIndexStore()
    index_store.load()

    raw_results = index_store.search(query_embedding, top_k=top_k)

    final_results = []

    for result in raw_results:
        item = fetch_item_by_vector_id(result["vector_id"])

        if item:
            item["score"] = result["score"]
            final_results.append(item)

    return final_results


def search_by_image(image_path: str, top_k: int = TOP_K):
    embedder = QwenVLEmbedder()

    query_embedding = embedder.encode_images([image_path])

    index_store = FaissIndexStore()
    index_store.load()

    raw_results = index_store.search(query_embedding, top_k=top_k)

    final_results = []

    for result in raw_results:
        item = fetch_item_by_vector_id(result["vector_id"])

        if item:
            item["score"] = result["score"]
            final_results.append(item)

    return final_results