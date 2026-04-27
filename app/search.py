from app.db import fetch_item_by_vector_id, search_exact_by_product_code
from app.embedder import QwenVLEmbedder
from app.index_store import FaissIndexStore
from app.config import TOP_K


_embedder_instance = None


def get_embedder():
    global _embedder_instance

    if _embedder_instance is None:
        _embedder_instance = QwenVLEmbedder()

    return _embedder_instance


def dedupe_results(results):
    seen = set()
    deduped = []

    for item in results:
        key = item["item_id"]

        if key in seen:
            continue

        seen.add(key)
        deduped.append(item)

    return deduped


def search_by_text(query: str, top_k: int = TOP_K, use_exact_search: bool = True):
    final_results = []

    # 1) Önce product_code exact/LIKE araması
    if use_exact_search:
        exact_results = search_exact_by_product_code(query)

        if exact_results:
            return exact_results[:top_k]

    # 2) Sonra FAISS semantic search
    embedder = get_embedder()

    query_embedding = embedder.encode_texts(
        [query],
        mode="query"
    )

    index_store = FaissIndexStore()
    index_store.load()

    # Aynı item text+image vector olarak iki kere dönebileceği için daha fazla çekiyoruz.
    raw_results = index_store.search(query_embedding, top_k=top_k * 3)

    for result in raw_results:
        item = fetch_item_by_vector_id(result["vector_id"])

        if item:
            item["score"] = result["score"]
            item["match_type"] = "semantic_faiss"
            final_results.append(item)

    final_results = dedupe_results(final_results)

    return final_results[:top_k]


def search_by_image(image_path: str, top_k: int = TOP_K):
    embedder = get_embedder()

    query_embedding = embedder.encode_images([image_path])

    index_store = FaissIndexStore()
    index_store.load()

    raw_results = index_store.search(query_embedding, top_k=top_k * 3)

    final_results = []

    for result in raw_results:
        item = fetch_item_by_vector_id(result["vector_id"])

        if item:
            item["score"] = result["score"]
            item["match_type"] = "image_faiss"
            final_results.append(item)

    final_results = dedupe_results(final_results)

    return final_results[:top_k]