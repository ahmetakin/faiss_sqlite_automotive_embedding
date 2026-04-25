from app.search import search_by_text


def print_results(results):
    print("\nSonuçlar:\n")

    for i, item in enumerate(results, start=1):
        print(f"{i}. Skor       : {item['score']:.4f}")
        print(f"   Tip        : {item['item_type']}")
        print(f"   Başlık     : {item['title']}")
        print(f"   Kategori   : {item['category']}")
        print(f"   Ürün kodu  : {item['product_code']}")
        print(f"   Kaynak     : {item['source']}")
        print(f"   Görsel     : {item['image_path']}")
        print(f"   İçerik     : {item['content']}")
        print(f"   Metadata   : {item['metadata']}")
        print("-" * 80)


if __name__ == "__main__":
    queries = [
        "elektrikli araç batarya garanti süresi kaç yıl",
        "araba aküsü görselini getir",
        "fren balatası aşınırsa ne olur",
        "motor yağı kaç kilometrede değişir",
        "BRK-PAD-FRONT ürün kodlu parça"
    ]

    for query in queries:
        print("\n" + "=" * 80)
        print("Sorgu:", query)
        results = search_by_text(query, top_k=5)
        print_results(results)