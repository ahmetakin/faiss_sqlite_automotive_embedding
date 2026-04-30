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
        "Honda civic fc5 fren balatası görselini getir",
        "ENGINE-OIL-AKN ürün kodlu parçayı açıkla",
        "en iyi araba aküsü markası hangisi",
        "en iyi araba fren balata markası hangisi",
        "en ucuz araba yağı markası hangisi",
        "fiyat performans akü öner"
    ]

    for question in questions:
        print("\n" + "=" * 80)
        print("Soru:", question)

        result = answer_with_rag(question, top_k=5)

        print("\nCevap:")
        print(result["answer"])

        print_sources(result["sources"])

#vektörledikten sonra cluster olusturma aşamasını vektörleyerek yap oluşturduğun clusterların merkezi öbeğinden bir vektör alıp bu vektorün gerçekten o clusterın yapısına uygunmu diye araştır
'''


================================================================================
Soru: Elektrikli araç batarya garantisi kaç yıl?
Embedding modeli yükleniyor...
Loading weights: 100%|███████████████████████████████████████████████| 625/625 [00:00<00:00, 729.47it/s]
Model hazır.
Model device: cuda:0

Cevap:
Elektrikli araç yüksek voltaj bataryaları **8 yıl** veya **160.000 kilometre** garanti kapsamındadır.

**Detaylar:**
*   **Garanti Koşulu:** Batarya kapasitesinin belirlenen eşik seviyesinin altına düşmesi gerekir.
*   **Garanti Dışı Durumlar:** Yetkisiz müdahale, fiziksel hasar veya uygunsuz şarj altyapısı.

**Ürün Bilgisi:**
*   **Ürün Kodu:** EV-BATTERY-WARRANTY
*   **Marka:** DemoAuto
*   **Kategori:** garanti
*   **Görsel:** None

Kaynaklar:
- semantic_faiss | Elektrikli Araç Batarya Garanti Politikası | EV-BATTERY-WARRANTY | None
- semantic_faiss | Araç Aküsü Görseli | BAT-12V-VRSTRT | images/car_battery_ever_start.jpeg
- semantic_faiss | Araç Aküsü Görseli | BAT-12V-PWRLN | images/car_battery_powerline.webp
- semantic_faiss | Araç Aküsü Görseli | BAT-12V-BOSCH | images/car_battery_bosch.png
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-SBS-FC5 | images/brake_pad_sbs_honda_civic_fc5_front.jpg

================================================================================
Soru: ENGINE-OIL-CASTROL ürün kodlu parçayı açıkla

Cevap:
**ENGINE-OIL-CASTROL** ürün kodlu parça, Castrol Magnetic 5w-30 marka motor yağıdır. Motorun iç parçalarını yağlayarak sürtünmeden kaynaklı aşınmayı önleyen ve motor ömrünü uzatan koruyucu sıvıdır.

**Ürün Detayları:**
*   **Marka:** CASTROL
*   **Ürün Kodu:** ENGINE-OIL-CASTROL
*   **Kategori:** motor_yagi_gorsel
*   **Görsel:** images/engine_oil_castrol_magnetic.jpg
*   **Fiyat:** 1050
*   **Rating:** 4.2
*   **Yorum Sayısı:** 389

*Not: Context içinde `recommendation_score` bulunmadığı için bu verilere göre en iyiyi kesin seçemem.*

Kaynaklar:
- product_code_exact | Motor yağı görseli | ENGINE-OIL-CASTROL | images/engine_oil_castrol_magnetic.jpg

================================================================================
Soru: Fren balatası aşınırsa ne olur?

Cevap:
Fren balatası aşındığında şu belirtiler görülebilir:

*   Frenleme sırasında **ötme sesi** çıkması,
*   Fren mesafesinde **uzama**,
*   Fren pedalında **sertleşme**,
*   Direksiyonda **titreşim** hissedilmesi.

Balata kalınlığı kritik seviyeye düştüğünde değişim yapılmalıdır.

**İlgili Ürünler (Honda Civic FC5 Uyumlu):**

1.  **BOSCH**
    *   Ürün Kodu: `BRK-PAD-FRONT-BOSCH-FC5`
    *   Görsel: `images/brake_pad_bosch_honda_civic_fc5_front.jpg`
    *   Fiyat: 2900 TL
    *   Garanti: 24 Ay
    *   Rating: 4.5 (330 Yorum)

2.  **OSIMCO**
    *   Ürün Kodu: `BRK-PAD-FRONT-OSIMCO-FC5`
    *   Görsel: `images/brake_pad_osimco_honda_civic_fc5_front.png`
    *   Fiyat: 2990 TL
    *   Garanti: 30 Ay
    *   Rating: 4.4 (300 Yorum)

3.  **BREMBO**
    *   Ürün Kodu: `BRK-PAD-FRONT-BREMBO-FC5`
    *   Görsel: `images/brake_pad_brembo_honda_civic_fc5_front.jpg`
    *   Fiyat: 3000 TL
    *   Garanti: 36 Ay
    *   Rating: 4.0 (370 Yorum)

4.  **SBS**
    *   Ürün Kodu: `BRK-PAD-FRONT-SBS-FC5`
    *   Görsel: `images/brake_pad_sbs_honda_civic_fc5_front.jpg`
    *   Fiyat: 2400 TL
    *   Garanti: 12 Ay
    *   Rating: 4.1 (320 Yorum)

Kaynaklar:
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-SBS-FC5 | images/brake_pad_sbs_honda_civic_fc5_front.jpg
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-OSIMCO-FC5 | images/brake_pad_osimco_honda_civic_fc5_front.png
- semantic_faiss | Fren Balatası Arıza Belirtileri | BRK-PAD-INFO | None
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-BREMBO-FC5 | images/brake_pad_brembo_honda_civic_fc5_front.jpg
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-BOSCH-FC5 | images/brake_pad_bosch_honda_civic_fc5_front.jpg

================================================================================
Soru: Araba aküsü görselini getir

Cevap:
Araba aküsü görselleri aşağıdadır:

1. **BOSCH 12V Araç Aküsü**
   - **Ürün Kodu:** BAT-12V-BOSCH
   - **Görsel:** `images/car_battery_bosch.png`
   - **Marka:** BOSCH
   - **Kategori:** yedek_parca_gorsel

2. **EVER START 12V Araç Aküsü**
   - **Ürün Kodu:** BAT-12V-VRSTRT
   - **Görsel:** `images/car_battery_ever_start.jpeg`
   - **Marka:** EVER START
   - **Kategori:** yedek_parca_gorsel

3. **POWERLINE 12V Araç Aküsü**
   - **Ürün Kodu:** BAT-12V-PWRLN
   - **Görsel:** `images/car_battery_powerline.webp`
   - **Marka:** POWERLINE
   - **Kategori:** yedek_parca_gorsel

Kaynaklar:
- metadata_filter | Araç Aküsü Görseli | BAT-12V-BOSCH | images/car_battery_bosch.png
- metadata_filter | Araç Aküsü Görseli | BAT-12V-VRSTRT | images/car_battery_ever_start.jpeg
- metadata_filter | Araç Aküsü Görseli | BAT-12V-PWRLN | images/car_battery_powerline.webp

================================================================================
Soru: BOSCH akü görselini getir

Cevap:
BOSCH aküsü için görsel yolu: `images/car_battery_bosch.png`

**Ürün Detayları:**
*   **Ürün Kodu:** BAT-12V-BOSCH
*   **Marka:** BOSCH
*   **Kategori:** Yedek Parça (Araç Aküsü)
*   **Görsel:** images/car_battery_bosch.png

Kaynaklar:
- metadata_filter | Araç Aküsü Görseli | BAT-12V-BOSCH | images/car_battery_bosch.png

================================================================================
Soru: Honda civic fc5 fren balatası görselini getir

Cevap:
Honda Civic FC5 fren balatası görselleri aşağıdadır:

1. **Bosch Fren Balatası**
   - **Ürün Kodu:** BRK-PAD-FRONT-BOSCH-FC5
   - **Görsel Yolu:** `images/brake_pad_bosch_honda_civic_fc5_front.jpg`
   - **Marka:** BOSCH
   - **Fiyat:** 2900
   - **Garanti:** 24 Ay
   - **Rating:** 4.5 (330 Yorum)

2. **SBS Fren Balatası**
   - **Ürün Kodu:** BRK-PAD-FRONT-SBS-FC5
   - **Görsel Yolu:** `images/brake_pad_sbs_honda_civic_fc5_front.jpg`
   - **Marka:** SBS
   - **Fiyat:** 2400
   - **Garanti:** 12 Ay
   - **Rating:** 4.1 (320 Yorum)

3. **Osimco Fren Balatası**
   - **Ürün Kodu:** BRK-PAD-FRONT-OSIMCO-FC5
   - **Görsel Yolu:** `images/brake_pad_osimco_honda_civic_fc5_front.png`
   - **Marka:** OSIMCO
   - **Fiyat:** 2990
   - **Garanti:** 30 Ay
   - **Rating:** 4.4 (300 Yorum)

4. **Brembo Fren Balatası**
   - **Ürün Kodu:** BRK-PAD-FRONT-BREMBO-FC5
   - **Görsel Yolu:** `images/brake_pad_brembo_honda_civic_fc5_front.jpg`
   - **Marka:** BREMBO
   - **Fiyat:** 3000
   - **Garanti:** 36 Ay
   - **Rating:** 4.0 (370 Yorum)

*Not: Context'te `recommendation_score` bulunmadığı için en iyiyi kesin seçemem. Ancak yukarıdaki ürünler Honda Civic FC5 kasa uyumlu ön fren balatalarıdır.*

Kaynaklar:
- metadata_filter | Fren Balatası Görseli | BRK-PAD-FRONT-BOSCH-FC5 | images/brake_pad_bosch_honda_civic_fc5_front.jpg
- metadata_filter | Fren Balatası Görseli | BRK-PAD-FRONT-SBS-FC5 | images/brake_pad_sbs_honda_civic_fc5_front.jpg
- metadata_filter | Fren Balatası Görseli | BRK-PAD-FRONT-OSIMCO-FC5 | images/brake_pad_osimco_honda_civic_fc5_front.png
- metadata_filter | Fren Balatası Görseli | BRK-PAD-FRONT-BREMBO-FC5 | images/brake_pad_brembo_honda_civic_fc5_front.jpg

================================================================================
Soru: ENGINE-OIL-AKN ürün kodlu parçayı açıkla

Cevap:
Verilen context bilgilerine göre **ENGINE-OIL-AKN** ürün koduna ait doğrudan bir kayıt bulunmamaktadır. Ancak, benzer ürün kodlu (ENGINE-OIL-TOTAL, ENGINE-OIL-SHELL, vb.) motor yağları için genel tanım ve alternatifler aşağıdadır:

**Motor Yağı Nedir?**
Motor yağı, motorun iç parçalarını yağlayarak sürtünmeden kaynaklı aşınmayı önleyen ve motor ömrünü uzatan koruyucu sıvıdır.

**Benzer Ürün Kodlu Alternatifler:**

1.  **Ürün Kodu:** ENGINE-OIL-TOTAL
    *   **Marka:** TOTAL
    *   **Görsel:** `images/engine_oil_total_quartz_5w_40.jpg`
    *   **Fiyat:** 1000
    *   **Rating:** 4.5
    *   **Yorum Sayısı:** 400

2.  **Ürün Kodu:** ENGINE-OIL-SHELL
    *   **Marka:** SHELL
    *   **Görsel:** `images/engine_oil_shell_helix_ultra_5w_40.jpeg`
    *   **Fiyat:** 1100
    *   **Rating:** 4.1
    *   **Yorum Sayısı:** 430

3.  **Ürün Kodu:** ENGINE-OIL-PPLUS
    *   **Marka:** PERFORMANCE PLUS
    *   **Görsel:** `images/engine_oil_performance_plus_5w_20.jpg`
    *   **Fiyat:** 950
    *   **Rating:** 4.0
    *   **Yorum Sayısı:** 385

4.  **Ürün Kodu:** ENGINE-OIL-CASTROL
    *   **Marka:** CASTROL
    *   **Görsel:** `images/engine_oil_castrol_magnetic.jpg`
    *   **Fiyat:** 1050
    *   **Rating:** 4.2
    *   **Yorum Sayısı:** 389

*Not: ENGINE-OIL-AKN için spesifik bir fiyat, rating veya garanti bilgisi context içinde yer almamaktadır.*

Kaynaklar:
- product_code_family_fallback | Motor yağı görseli | ENGINE-OIL-TOTAL | images/engine_oil_total_quartz_5w_40.jpg
- product_code_family_fallback | Motor yağı görseli | ENGINE-OIL-SHELL | images/engine_oil_shell_helix_ultra_5w_40.jpeg
- product_code_family_fallback | Motor yağı görseli | ENGINE-OIL-PPLUS | images/engine_oil_performance_plus_5w_20.jpg
- product_code_family_fallback | Motor yağı görseli | ENGINE-OIL-CASTROL | images/engine_oil_castrol_magnetic.jpg

================================================================================
Soru: en iyi araba aküsü markası hangisi

Cevap:
Verilen bilgilere göre en iyi araba aküsü markasını kesin seçemem. Ancak **recommendation_score** (öneri skoru) baz alındığında sıralama ve karşılaştırma şöyledir:

1.  **POWERLINE** (Öneri Skoru: 0.8256)
    *   **Ürün Kodu:** BAT-12V-PWRLN
    *   **Görsel:** images/car_battery_powerline.webp
    *   **Rating:** 4.3
    *   **Yorum Sayısı:** 330
    *   **Garanti:** 36 Ay
    *   **Fiyat:** 2900
    *   **CCA:** 670

2.  **BOSCH** (Öneri Skoru: 0.787)
    *   **Ürün Kodu:** BAT-12V-BOSCH
    *   **Görsel:** images/car_battery_bosch.png
    *   **Rating:** 4.7
    *   **Yorum Sayısı:** 320
    *   **Garanti:** 24 Ay
    *   **Fiyat:** 2850
    *   **CCA:** 680

3.  **EVER START** (Öneri Skoru: 0.6697)
    *   **Ürün Kodu:** BAT-12V-VRSTRT
    *   **Görsel:** images/car_battery_ever_start.jpeg
    *   **Rating:** 4.1
    *   **Yorum Sayısı:** 322
    *   **Garanti:** 12 Ay
    *   **Fiyat:** 3100
    *   **CCA:** 660

**Karşılaştırma Özeti:**
*   **En Yüksek Öneri Skoru:** POWERLINE (0.8256)
*   **En Yüksek Rating:** BOSCH (4.7)
*   **En Uzun Garanti:** POWERLINE (36 Ay)
*   **En Yüksek CCA:** BOSCH (680)
*   **En Düşük Fiyat:** BOSCH (2850)

POWERLINE, genel öneri skoru ve garanti süresi açısından öne çıkarken; BOSCH daha yüksek kullanıcı puanı (rating), daha yüksek soğuk marş akımı (CCA) ve daha uygun fiyat sunmaktadır.

Kaynaklar:
- recommendation_candidates | Araç Aküsü Görseli | BAT-12V-PWRLN | images/car_battery_powerline.webp
- recommendation_candidates | Araç Aküsü Görseli | BAT-12V-BOSCH | images/car_battery_bosch.png
- recommendation_candidates | Araç Aküsü Görseli | BAT-12V-VRSTRT | images/car_battery_ever_start.jpeg
- recommendation_candidates | Elektrikli Araç Batarya Garanti Politikası | EV-BATTERY-WARRANTY | None

================================================================================
Soru: en iyi araba fren balata markası hangisi

Cevap:
Verilen bilgilere göre en iyi fren balatası markasını kesin olarak seçemem. Ancak **recommendation_score** (öneri skoru) baz alındığında sıralama ve karşılaştırma şöyledir:

1.  **BREMBO** (Öneri Skoru: 0.671)
    *   **Ürün Kodu:** BRK-PAD-FRONT-BREMBO-FC5
    *   **Görsel:** images/brake_pad_brembo_honda_civic_fc5_front.jpg
    *   **Rating:** 4.0
    *   **Yorum Sayısı:** 370
    *   **Garanti:** 36 Ay
    *   **Fiyat:** 3000

2.  **OSIMCO** (Öneri Skoru: 0.6449)
    *   **Ürün Kodu:** BRK-PAD-FRONT-OSIMCO-FC5
    *   **Görsel:** images/brake_pad_osimco_honda_civic_fc5_front.png
    *   **Rating:** 4.4
    *   **Yorum Sayısı:** 300
    *   **Garanti:** 30 Ay
    *   **Fiyat:** 2990

3.  **BOSCH** (Öneri Skoru: 0.6293)
    *   **Ürün Kodu:** BRK-PAD-FRONT-BOSCH-FC5
    *   **Görsel:** images/brake_pad_bosch_honda_civic_fc5_front.jpg
    *   **Rating:** 4.5
    *   **Yorum Sayısı:** 330
    *   **Garanti:** 24 Ay
    *   **Fiyat:** 2900

4.  **SBS** (Öneri Skoru: 0.5417)
    *   **Ürün Kodu:** BRK-PAD-FRONT-SBS-FC5
    *   **Görsel:** images/brake_pad_sbs_honda_civic_fc5_front.jpg
    *   **Rating:** 4.1
    *   **Yorum Sayısı:** 320
    *   **Garanti:** 12 Ay
    *   **Fiyat:** 2400

**Özet Karşılaştırma:**
*   **En Yüksek Öneri Skoru:** BREMBO
*   **En Yüksek Rating:** BOSCH (4.5)
*   **En Uzun Garanti:** BREMBO (36 Ay)
*   **En Düşük Fiyat:** SBS (2400)

Honda Civic FC5 kasa için ön fren balatası arıyorsanız, öneri skoruna göre **BREMBO** ilk sırada yer almaktadır.

Kaynaklar:
- recommendation_candidates | Fren Balatası Görseli | BRK-PAD-FRONT-BREMBO-FC5 | images/brake_pad_brembo_honda_civic_fc5_front.jpg
- recommendation_candidates | Fren Balatası Görseli | BRK-PAD-FRONT-OSIMCO-FC5 | images/brake_pad_osimco_honda_civic_fc5_front.png
- recommendation_candidates | Fren Balatası Görseli | BRK-PAD-FRONT-BOSCH-FC5 | images/brake_pad_bosch_honda_civic_fc5_front.jpg
- recommendation_candidates | Fren Balatası Görseli | BRK-PAD-FRONT-SBS-FC5 | images/brake_pad_sbs_honda_civic_fc5_front.jpg
- recommendation_candidates | Fren Balatası Arıza Belirtileri | BRK-PAD-INFO | None

================================================================================
Soru: en ucuz araba yağı markası hangisi

Cevap:
Verilen bilgilere göre en ucuz araba yağı markası **Performance Plus**'tır.

Context içindeki motor yağları için fiyat karşılaştırması şöyledir:

| Marka | Ürün Kodu | Fiyat | Rating | Yorum Sayısı |
| :--- | :--- | :--- | :--- | :--- |
| **Performance Plus** | ENGINE-OIL-PPLUS | **950** | 4.0 | 385 |
| Total | ENGINE-OIL-TOTAL | 1000 | 4.5 | 400 |
| Castrol | ENGINE-OIL-CASTROL | 1050 | 4.2 | 389 |
| Shell | ENGINE-OIL-SHELL | 1100 | 4.1 | 430 |

**Öneri:** Performance Plus 5w-20 (Ürün Kodu: ENGINE-OIL-PPLUS) en uygun fiyat seçeneğidir.
**Görsel:** images/engine_oil_performance_plus_5w_20.jpg

Kaynaklar:
- semantic_faiss | Motor yağı görseli | ENGINE-OIL-CASTROL | images/engine_oil_castrol_magnetic.jpg
- semantic_faiss | Motor yağı görseli | ENGINE-OIL-TOTAL | images/engine_oil_total_quartz_5w_40.jpg
- semantic_faiss | Motor yağı görseli | ENGINE-OIL-SHELL | images/engine_oil_shell_helix_ultra_5w_40.jpeg
- semantic_faiss | Motor yağı görseli | ENGINE-OIL-PPLUS | images/engine_oil_performance_plus_5w_20.jpg
- semantic_faiss | Fren Balatası Görseli | BRK-PAD-FRONT-SBS-FC5 | images/brake_pad_sbs_honda_civic_fc5_front.jpg

================================================================================
Soru: fiyat performans akü öner

Cevap:
Fiyat performans kriterine göre en yüksek öneri skoruna sahip ürün **POWERLINE** markalı aküdür. Ancak diğer seçeneklerin detaylı karşılaştırması aşağıdadır:

**1. POWERLINE (BAT-12V-PWRLN)**
*   **Öneri Skoru:** 0.8256 (En Yüksek)
*   **Fiyat:** 2.900 TL
*   **Garanti:** 36 Ay
*   **Rating:** 4.3 (330 Yorum)
*   **CCA:** 670
*   **Görsel:** images/car_battery_powerline.webp

**2. BOSCH (BAT-12V-BOSCH)**
*   **Öneri Skoru:** 0.787
*   **Fiyat:** 2.850 TL
*   **Garanti:** 24 Ay
*   **Rating:** 4.7 (320 Yorum)
*   **CCA:** 680
*   **Görsel:** images/car_battery_bosch.png

**3. EVER START (BAT-12V-VRSTRT)**
*   **Öneri Skoru:** 0.6697
*   **Fiyat:** 3.100 TL
*   **Garanti:** 12 Ay
*   **Rating:** 4.1 (322 Yorum)
*   **CCA:** 660
*   **Görsel:** images/car_battery_ever_start.jpeg

**Değerlendirme:**
POWERLINE, en yüksek öneri skoru (0.8256) ve en uzun garanti süresi (36 ay) ile öne çıkmaktadır. BOSCH ise daha yüksek kullanıcı puanı (4.7) ve daha yüksek CCA değerine (680) sahip olup fiyatı en düşük olan seçenektir. EVER START ise en yüksek fiyata sahip ve en kısa garanti süresine sahiptir.

*Not: Bu verilere göre en iyiyi kesin seçemem ancak öneri skoruna göre POWERLINE ilk sırada yer almaktadır.*

Kaynaklar:
- recommendation_candidates | Araç Aküsü Görseli | BAT-12V-PWRLN | images/car_battery_powerline.webp
- recommendation_candidates | Araç Aküsü Görseli | BAT-12V-BOSCH | images/car_battery_bosch.png
- recommendation_candidates | Araç Aküsü Görseli | BAT-12V-VRSTRT | images/car_battery_ever_start.jpeg
- recommendation_candidates | Elektrikli Araç Batarya Garanti Politikası | EV-BATTERY-WARRANTY | None
(.llmproject_env) user@user:~/ahmet-ai/faiss_sqlite_automotive$


'''