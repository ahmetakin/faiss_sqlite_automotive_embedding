from app.rag import answer_with_rag


def print_sources(sources):
    print("\nKaynaklar:")

    for item in sources:
        print(
            "-",
            item.get("match_type"),
            "|",
            item.get("title"),
            "|",
            item.get("product_code"),
            "|",
            item.get("image_path")
        )


if __name__ == "__main__":
    questions = [
        "Elektrikli araç batarya garantisi kaç yıl?",
        "ENGINE-OIL-CASTROL ürün kodlu parçayı açıkla",
        "Fren balatası aşınırsa ne olur?",
        "Araba aküsü görselini getir",
        "BOSCH akü görselini getir",
        "Honda civic fc5 fren balatası görselini getir"
    ]

    for question in questions:
        print("\n" + "=" * 80)
        print("Soru:", question)

        result = answer_with_rag(question, top_k=5)

        print("\nCevap:")
        print(result["answer"])

        print_sources(result["sources"])


'''
(.llmproject_env) user@user:~/ahmet-ai/faiss_sqlite_automotive$ PYTHONPATH=. python scripts/05_hybrid_rag_demo.py

================================================================================
Soru: Elektrikli araç batarya garantisi kaç yıl?
Embedding modeli yükleniyor...
Loading weights: 100%|████████████████████████████████████████████████████| 625/625 [00:01<00:00, 571.60it/s]
Model hazır.
Model device: cuda:0

Cevap:
Elektrikli araç yüksek voltaj bataryaları **8 yıl** veya **160.000 kilometre** garanti kapsamındadır.

*   **Ürün Kodu:** EV-BATTERY-WARRANTY
*   **Marka:** DemoAuto
*   **Kategori:** garanti
*   **Görsel:** None

Kaynaklar:
- semantic_faiss | Elektrikli Araç Batarya Garanti Politikası | EV-BATTERY-WARRANTY | None
- semantic_faiss | Araç Aküsü Görseli | BAT-12V-PWRLN | images/car_battery_powerline.webp
- semantic_faiss | Araç Aküsü Görseli | BAT-12V-VRSTRT | images/car_battery_ever_start.jpeg
- semantic_faiss | Araç Aküsü Görseli | BAT-12V-BOSCH | images/car_battery_bosch.png
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-SBS-FC5 | images/brake_pad_sbs_honda_civic_fc5_front.jpg

================================================================================
Soru: ENGINE-OIL-CASTROL ürün kodlu parçayı açıkla

Cevap:
ENGINE-OIL-CASTROL ürün kodlu parça, Castrol Magnetic 5w-30 marka motor yağıdır. Motorun iç parçalarını yağlayarak sürtünmeden kaynaklı aşınmayı önleyen ve motor ömrünü uzatan koruyucu sıvıdır.

*   **Marka:** CASTROL
*   **Kategori:** motor_yagi_gorsel
*   **Ürün Kodu:** ENGINE-OIL-CASTROL
*   **Görsel:** images/engine_oil_castrol_magnetic.jpg

Kaynaklar:
- product_code_exact | Motor yağı görseli | ENGINE-OIL-CASTROL | images/engine_oil_castrol_magnetic.jpg

================================================================================
Soru: Fren balatası aşınırsa ne olur?

Cevap:
Fren balatası aşındığında şu belirtiler görülebilir:
*   Frenleme sırasında ötme sesi
*   Fren mesafesinde uzama
*   Pedalda sertleşme
*   Direksiyonda titreşim

Balata kalınlığı kritik seviyeye düştüğünde değişim yapılmalıdır.

**Ürün Kodu:** BRK-PAD-INFO
**Marka:** DemoAuto
**Kategori:** teknik_bilgi
**Görsel:** None

Kaynaklar:
- semantic_faiss | Fren Balatası Arıza Belirtileri | BRK-PAD-INFO | None
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-SBS-FC5 | images/brake_pad_sbs_honda_civic_fc5_front.jpg
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-OSIMCO-FC5 | images/brake_pad_osimco_honda_civic_fc5_front.png
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-BREMBO-FC5 | images/brake_pad_brembo_honda_civic_fc5_front.jpg
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-BOSCH-FC5 | images/brake_pad_bosch_honda_civic_fc5_front.jpg

================================================================================
Soru: Araba aküsü görselini getir

Cevap:
Araba aküsü görseli aşağıdadır:

*   **Ürün Kodu:** BAT-12V-PWRLN
*   **Marka:** POWERLINE
*   **Kategori:** yedek_parca_gorsel
*   **Görsel Yolu:** `images/car_battery_powerline.webp`

**Açıklama:** 12V araç aküsü, otomotiv marş sistemi ve elektrik besleme parçasıdır.

Kaynaklar:
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-SBS-FC5 | images/brake_pad_sbs_honda_civic_fc5_front.jpg
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-OSIMCO-FC5 | images/brake_pad_osimco_honda_civic_fc5_front.png
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-BREMBO-FC5 | images/brake_pad_brembo_honda_civic_fc5_front.jpg
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-BOSCH-FC5 | images/brake_pad_bosch_honda_civic_fc5_front.jpg
- semantic_faiss | Araç Aküsü Görseli | BAT-12V-PWRLN | images/car_battery_powerline.webp

================================================================================
Soru: BOSCH akü görselini getir

Cevap:
Bulunan context'te doğrudan "BOSCH" markalı bir **akü** görseli bulunmamaktadır. Context'te yer alan tek akü görseli **POWERLINE** markalıdır.

Ancak, **BOSCH** markalı bir parça görseli (Fren Balatası) mevcuttur:

*   **Marka:** BOSCH
*   **Kategori:** Fren Balatası (Yedek Parça)
*   **Ürün Kodu:** BRK-PAD-FRONT-BOSCH-FC5
*   **Görsel Yolu:** `images/brake_pad_bosch_honda_civic_fc5_front.jpg`

Eğer kullanıcı genel olarak BOSCH görseli istiyorsa yukarıdaki fren balatası görseli kullanılabilir. Eğer spesifik olarak akü isteniyorsa, context'te BOSCH akü görseli yoktur.

Kaynaklar:
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-OSIMCO-FC5 | images/brake_pad_osimco_honda_civic_fc5_front.png
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-BOSCH-FC5 | images/brake_pad_bosch_honda_civic_fc5_front.jpg
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-SBS-FC5 | images/brake_pad_sbs_honda_civic_fc5_front.jpg
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-BREMBO-FC5 | images/brake_pad_brembo_honda_civic_fc5_front.jpg
- semantic_faiss | Araç Aküsü Görseli | BAT-12V-PWRLN | images/car_battery_powerline.webp

================================================================================
Soru: Honda civic fc5 fren balatası görselini getir

Cevap:
Honda Civic FC5 için ön fren balatası görselleri aşağıdadır:

*   **SBS Marka**
    *   Ürün Kodu: `BRK-PAD-FRONT-SBS-FC5`
    *   Görsel Yolu: `images/brake_pad_sbs_honda_civic_fc5_front.jpg`

*   **OSIMCO Marka**
    *   Ürün Kodu: `BRK-PAD-FRONT-OSIMCO-FC5`
    *   Görsel Yolu: `images/brake_pad_osimco_honda_civic_fc5_front.png`

*   **BOSCH Marka**
    *   Ürün Kodu: `BRK-PAD-FRONT-BOSCH-FC5`
    *   Görsel Yolu: `images/brake_pad_bosch_honda_civic_fc5_front.jpg`

*   **BREMBO Marka**
    *   Ürün Kodu: `BRK-PAD-FRONT-BREMBO-FC5`
    *   Görsel Yolu: `images/brake_pad_brembo_honda_civic_fc5_front.jpg`

Tüm ürünler disk fren sistemi içindir ve Honda Civic FC5 kasa uyumludur.

Kaynaklar:
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-SBS-FC5 | images/brake_pad_sbs_honda_civic_fc5_front.jpg
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-OSIMCO-FC5 | images/brake_pad_osimco_honda_civic_fc5_front.png
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-BOSCH-FC5 | images/brake_pad_bosch_honda_civic_fc5_front.jpg
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-BREMBO-FC5 | images/brake_pad_brembo_honda_civic_fc5_front.jpg
- semantic_faiss | Araç Aküsü Görseli | BAT-12V-PWRLN | images/car_battery_powerline.webp


'''