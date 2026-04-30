from app.hybrid_search import hybrid_search
from app.llm_client import ask_llm


def format_context(results):
    blocks = []

    for i, item in enumerate(results, start=1):
        block = f"""
[Kaynak {i}]
Eşleşme tipi: {item.get("match_type")}
Tip: {item.get("item_type")}
Başlık: {item.get("title")}
Kategori: {item.get("category")}
Ürün kodu: {item.get("product_code")}
Kaynak: {item.get("source")}
Görsel: {item.get("image_path")}
İçerik: {item.get("content")}
Metadata: {item.get("metadata")}
Skor: {item.get("score")}
Final skor: {item.get("final_score")}
Öneri skoru: {item.get("recommendation_score")}
Rating skoru: {item.get("rating_score")}
Yorum skoru: {item.get("review_score")}
Garanti skoru: {item.get("warranty_score")}
Semantic bileşen: {item.get("semantic_component")}
CCA skoru: {item.get("cca_score")}
Fiyat skoru: {item.get("price_score")}
""".strip()

        blocks.append(block)

    return "\n\n".join(blocks)


def answer_with_rag(question: str, top_k: int = 5):
    results = hybrid_search(question, top_k=top_k)
    context = format_context(results)

    messages = [
        {
            "role": "system",
            "content": (
                "Sen otomotiv şirketi için çalışan uzman bir teknik destek asistanısın. "
                "Sadece verilen context bilgilerine dayanarak cevap ver. "
                "Context içinde bilgi yoksa açıkça belirt. "
                "Ürün kodu, marka, kategori ve görsel yolu varsa cevaba ekle. "
                "Eğer kullanıcı görsel istiyorsa, görsel yolunu özellikle belirt."
                "Eğer kullanıcı 'en iyi', 'öner', 'tavsiye', 'hangisi daha iyi' gibi karşılaştırma sorusu sorarsa, "
                "context içinde puan, fiyat, yorum, performans, garanti, satış adedi gibi açık bir karşılaştırma metriği yoksa "
                "'bu verilere göre en iyiyi kesin seçemem' de. "
                "Sonra context içindeki adayları listele."
                "Eğer context içinde recommendation_score varsa, öneri cevabını bu skora göre ver. "
                "En yüksek recommendation_score değerine sahip ürünü önce belirt. "
                "Ancak cevabında rating, yorum sayısı, garanti ve fiyat bilgilerini de karşılaştırmalı göster."
                "Karşılaştırma yaparken recommendation_score, rating, yorum sayısı, garanti, CCA ve fiyat alanlarını dikkate al. "
            )
        },
        {
            "role": "user",
            "content": f"""
Kullanıcı sorusu:
{question}

Bulunan context:
{context}

Görev:
Kullanıcının sorusunu kısa, net ve teknik olarak doğru cevapla.
""".strip()
        }
    ]

    answer = ask_llm(messages)

    return {
        "question": question,
        "answer": answer,
        "sources": results
    }