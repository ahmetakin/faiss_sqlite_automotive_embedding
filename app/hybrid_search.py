from app.router import detect_query_intent
from app.db import (
    search_items_by_product_code,
    search_items_by_metadata_like,
    fetch_item_by_vector_id
)
from app.search import search_by_text


def deduplicate_results(results):
    seen = set()
    unique_results = []

    for item in results:
        key = item.get("item_id") or item.get("vector_id")

        if key in seen:
            continue

        seen.add(key)
        unique_results.append(item)

    return unique_results


def filter_only_images(results):
    return [
        item for item in results
        if item.get("item_type") == "image"
    ]


def hybrid_search(query: str, top_k: int = 5):
    route = detect_query_intent(query)

    final_results = []

    # 1) Ürün kodu varsa önce SQLite exact search
    if route["intent"] == "product_code":
        for code in route["product_codes"]:
            exact_results = search_items_by_product_code(code)
            final_results.extend(exact_results)

        if final_results:
            return deduplicate_results(final_results)[:top_k]

    # 2) Görsel isteği varsa önce metadata LIKE ile image kayıtlarında ara
    if route["intent"] == "image_search":
        words = query.replace("görselini", "").replace("görsel", "").strip()

        metadata_results = search_items_by_metadata_like(
            query=words,
            only_images=True,
            limit=top_k
        )

        final_results.extend(metadata_results)

        # Sonra FAISS semantic search
        semantic_results = search_by_text(query, top_k=top_k * 2)
        semantic_results = filter_only_images(semantic_results)

        for item in semantic_results:
            item["match_type"] = item.get("match_type", "faiss_semantic_image")
            final_results.append(item)

        return deduplicate_results(final_results)[:top_k]

    # 3) Normal semantic search
    semantic_results = search_by_text(query, top_k=top_k)

    for item in semantic_results:
        item["match_type"] = item.get("match_type", "faiss_semantic")

    return deduplicate_results(semantic_results)[:top_k]