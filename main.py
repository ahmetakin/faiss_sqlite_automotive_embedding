from app.search import search_by_text, search_by_image


def print_results(results):
    if not results:
        print("Sonuç bulunamadı.\n")
        return

    for i, item in enumerate(results, start=1):
        print(f"\n{i}. [{item['score']:.4f}] {item['title']}")
        print(f"   Tip       : {item['item_type']}")
        print(f"   Kategori  : {item['category']}")
        print(f"   Ürün kodu : {item['product_code']}")
        print(f"   Görsel    : {item['image_path']}")
        print(f"   İçerik    : {item['content']}")


def main():
    print("FAISS + SQLite + Qwen3-VL-Embedding-2B")
    print("1: Metin sorgusu")
    print("2: Görsel sorgusu")
    print("q: Çıkış")

    while True:
        mode = input("\nSeçim: ").strip()

        if mode.lower() == "q":
            break

        if mode == "1":
            query = input("Metin sorgusu: ").strip()
            results = search_by_text(query, top_k=5)
            print_results(results)

        elif mode == "2":
            image_path = input("Görsel path: ").strip()
            results = search_by_image(image_path, top_k=5)
            print_results(results)

        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    main()