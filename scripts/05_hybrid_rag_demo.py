from app.rag import answer_with_rag
import json
from datetime import datetime

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

def save_results_to_json(results, filename=None):
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"rag_results_{timestamp}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n📁 JSON kaydedildi: {filename}")


if __name__ == "__main__":
    questions = [
        "Elektrikli araç batarya garantisi kaç yıl?",
        "Araç aküsü garanti süresi kaç yıl?",
        "Motor garantisi kaç yıl?",
        "Şanzıman garanti şartları nelerdir?",
        "Elektrik sistemleri garanti kapsamında mı?",
        "Fren balatası aşınırsa ne olur?",
        "Fren hidroliği nem oranı artarsa ne olur?",
        "Vakum pompası arızalanırsa fren nasıl etkilenir?",
        "Honda civic fc5 fren balatası görselini getir",
        "BREMBO fren diski görselini getir",
        "Debriyaj seti görselini getir",
        "Akü şarj cihazı görselini getir",
        "Araba aküsü görselini getir",
        "BOSCH akü görselini getir",
        "en iyi araba aküsü markası hangisi",
        "fiyat performans akü öner",
        "en iyi fren balatası hangisi",
        "en iyi fren diski hangisi",
        "en ucuz motor yağı hangisi",
        "en iyi motor yağı hangisi",
        "ENGINE-OIL-AKN ürün kodlu parçayı açıkla",
        "BRAKE-DISC-BREMBO ürün kodlu parçayı açıkla",
        "CLUTCH-KIT-LUK ürün kodlu parçayı açıkla",
        "AIR-FIL-MANN ürün kodlu parçayı açıkla",
        "turbo arızasında ne olur?",
        "DPF nasıl temizlenir?",
        "Start stop sistemi neden devreye girmez?",
        "ABS ışığı yanarsa ne anlama gelir?",
        "triger kayışı koparsa ne olur?",
        "yağ lambası kırmızı yanarsa ne yapılmalı?"
    ]


    all_results = []
    
    for question in questions:
        print("\n" + "=" * 80)
        print("Soru:", question)

        result = answer_with_rag(question, top_k=5)

        print("\nCevap:")
        print(result["answer"])

        print_sources(result["sources"])

        all_results.append(result)

    # 🔥 BURASI ÖNEMLİ
    save_results_to_json(all_results)

#vektörledikten sonra cluster olusturma aşamasını vektörleyerek yap oluşturduğun clusterların merkezi öbeğinden bir vektör alıp bu vektorün gerçekten o clusterın yapısına uygunmu diye araştır
'''

(.llmproject_env) user@user:~/ahmet-ai/faiss_sqlite_automotive$ PYTHONPATH=. python scripts/05_hybrid_rag_demo.py

================================================================================
Soru: Elektrikli araç batarya garantisi kaç yıl?
Embedding modeli yükleniyor...
Loading weights: 100%|██████████████████████████████████████████████████████████████| 625/625 [00:01<00:00, 580.86it/s]
Model hazır.
Model device: cuda:0
Metinler işleniyor: 100%|████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  3.60it/s]

Cevap:
Context bilgilerine göre elektrikli araç batarya garantisi süresi belirtilmemiştir.

Kaynaklar:

================================================================================
Soru: ENGINE-OIL-CASTROL ürün kodlu parçayı açıkla

Cevap:
ENGINE-OIL-CASTROL ürün kodlu parça, Castrol Magnetic 5w-30 marka motor yağıdır. Motorun iç parçalarını yağlayarak sürtünmeden kaynaklı aşınmayı önleyen ve motor ömrünü uzatan koruyucu sıvıdır.

**Ürün Detayları:**
*   **Marka:** CASTROL
*   **Ürün Kodu:** ENGINE-OIL-CASTROL
*   **Kategori:** motor_yagi_gorsel
*   **Görsel:** images/engine_oil_castrol_magnetic.jpg
*   **Fiyat:** 1050
*   **Rating:** 4.2
*   **Yorum Sayısı:** 389
*   **Garanti:** Bilgi context'te mevcut değil.
*   **Öneri Skoru:** None

*Not: Context'te başka karşılaştırılabilir ürünler olmadığı için en iyi seçimi kesin belirleyemem.*

Kaynaklar:
- product_code_exact | Motor yağı görseli | ENGINE-OIL-CASTROL | images/engine_oil_castrol_magnetic.jpg

================================================================================
Soru: Fren balatası aşınırsa ne olur?
Metinler işleniyor: 100%|████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 15.74it/s]

Cevap:
Fren balatası aşındığında frenleme performansı düşer ve fren pedalında sertleşme veya titreme gibi hissedilebilir değişiklikler yaşanabilir. Ayrıca, balata bitene kadar metalin metale sürtünmesi sonucu "cızırtı" veya "gıcırtı" şeklinde yüksek sesli uyarı sesleri duyulabilir. Bu durum, fren diskinin de zarar görmesine ve daha yüksek onarım maliyetlerine yol açabilir.

*   **Marka:** -
*   **Ürün Kodu:** -
*   **Kategori:** Fren Balatası
*   **Görsel Yolu:** -

*Not: Context bilgisi genel bir soru olduğu için spesifik bir ürün kodu veya görseli bulunmamaktadır.*

Kaynaklar:

================================================================================
Soru: Araba aküsü görselini getir

Cevap:
Araba aküsü görselleri aşağıdadır:

1. **BOSCH 12V Araç Aküsü**
   - **Ürün Kodu:** BAT-12V-BOSCH
   - **Görsel:** `images/car_battery_bosch.png`
   - **Detaylar:** 24 ay garanti, 4.7 puan (320 yorum), 2850 TL, 680 CCA.

2. **EVER START 12V Araç Aküsü**
   - **Ürün Kodu:** BAT-12V-VRSTRT
   - **Görsel:** `images/car_battery_ever_start.jpeg`
   - **Detaylar:** 12 ay garanti, 4.1 puan (322 yorum), 3100 TL, 660 CCA.

3. **POWERLINE 12V Araç Aküsü**
   - **Ürün Kodu:** BAT-12V-PWRLN
   - **Görsel:** `images/car_battery_powerline.webp`
   - **Detaylar:** 36 ay garanti, 4.3 puan (330 yorum), 2900 TL, 670 CCA.

*Not: Context'te `recommendation_score` bulunmadığı için bu verilere göre en iyiyi kesin seçemem. Ancak karşılaştırma yapmak gerekirse; POWERLINE en uzun garantisi (36 ay) ve en yüksek fiyatı (3100 TL ile EVER START'tan sonra) ile öne çıkarken, BOSCH en yüksek puanı (4.7) ve en uygun fiyatı (2850 TL) sunmaktadır.*

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
*   **Açıklama:** 12V araç aküsü, otomotiv marş sistemi ve elektrik besleme parçası.
*   **Metadata:** {'brand': 'BOSCH', 'part_group': 'battery', 'voltage': '12V', 'warranty_months': 24, 'rating': 4.7, 'review_count': 320, 'price': 2850, 'cold_cranking_amp': 680}

Kaynaklar:
- metadata_filter | Araç Aküsü Görseli | BAT-12V-BOSCH | images/car_battery_bosch.png

================================================================================
Soru: Honda civic fc5 fren balatası görselini getir
Metinler işleniyor: 100%|████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 15.57it/s]

Cevap:
Honda Civic FC5 fren balatası görseli:
`/images/honda_civic_fc5_brake_pads.jpg`

*   **Marka:** Honda
*   **Model:** Civic FC5
*   **Kategori:** Fren Balatası
*   **Ürün Kodu:** FC5-BP-001

Kaynaklar:

================================================================================
Soru: ENGINE-OIL-AKN ürün kodlu parçayı açıkla

Cevap:
Verilen context bilgilerine göre **ENGINE-OIL-AKN** ürün koduna ait doğrudan bir açıklama bulunmamaktadır. Ancak, benzer ürün kodlu (ENGINE-OIL-*) motor yağları genel olarak motorun iç parçalarını yağlayarak sürtünmeden kaynaklı aşınmayı önleyen ve motor ömrünü uzatan koruyucu sıvılardır.

**ENGINE-OIL-AKN** için spesifik marka, fiyat veya görsel bilgisi context'te yer almamaktadır.

*   **Ürün Kodu:** ENGINE-OIL-AKN
*   **Marka:** Context'te belirtilmemiş
*   **Kategori:** Motor Yağı
*   **Görsel Yolu:** Context'te belirtilmemiş

*(Not: Context'te ENGINE-OIL-TOTAL, ENGINE-OIL-SHELL, ENGINE-OIL-PPLUS ve ENGINE-OIL-CASTROL ürünleri için detaylı bilgiler bulunmaktadır.)*

Kaynaklar:
- product_code_family_fallback | Motor yağı görseli | ENGINE-OIL-TOTAL | images/engine_oil_total_quartz_5w_40.jpg
- product_code_family_fallback | Motor yağı görseli | ENGINE-OIL-SHELL | images/engine_oil_shell_helix_ultra_5w_40.jpeg
- product_code_family_fallback | Motor yağı görseli | ENGINE-OIL-PPLUS | images/engine_oil_performance_plus_5w_20.jpg
- product_code_family_fallback | Motor yağı görseli | ENGINE-OIL-CASTROL | images/engine_oil_castrol_magnetic.jpg

================================================================================
Soru: en iyi araba aküsü markası hangisi

Cevap:
Verilen bilgilere göre öneri skoru (recommendation_score) en yüksek olan marka **POWERLINE**'dır. Ancak diğer kriterlere göre karşılaştırma şöyledir:

1.  **POWERLINE** (Öneri Skoru: 0.8256)
    *   **Ürün Kodu:** BAT-12V-PWRLN
    *   **Görsel:** images/car_battery_powerline.webp
    *   **Rating:** 4.3 (330 yorum)
    *   **Garanti:** 36 Ay
    *   **Fiyat:** 2900
    *   **CCA:** 670

2.  **BOSCH** (Öneri Skoru: 0.787)
    *   **Ürün Kodu:** BAT-12V-BOSCH
    *   **Görsel:** images/car_battery_bosch.png
    *   **Rating:** 4.7 (320 yorum)
    *   **Garanti:** 24 Ay
    *   **Fiyat:** 2850
    *   **CCA:** 680

3.  **EVER START** (Öneri Skoru: 0.6697)
    *   **Ürün Kodu:** BAT-12V-VRSTRT
    *   **Görsel:** images/car_battery_ever_start.jpeg
    *   **Rating:** 4.1 (322 yorum)
    *   **Garanti:** 12 Ay
    *   **Fiyat:** 3100
    *   **CCA:** 660

**Özet:** Öneri skoru en yüksek olan **POWERLINE**'dır. Ancak en yüksek kullanıcı puanı (4.7) ve en yüksek CCA değerine (680) **BOSCH** sahiptir. En uzun garanti süresi ise yine **POWERLINE**'da (36 ay) bulunur.

Kaynaklar:
- recommendation_candidates | Araç Aküsü Görseli | BAT-12V-PWRLN | images/car_battery_powerline.webp
- recommendation_candidates | Araç Aküsü Görseli | BAT-12V-BOSCH | images/car_battery_bosch.png
- recommendation_candidates | Araç Aküsü Görseli | BAT-12V-VRSTRT | images/car_battery_ever_start.jpeg

================================================================================
Soru: en iyi araba fren balata markası hangisi
Metinler işleniyor: 100%|████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 13.10it/s]

Cevap:
Verilen context bilgilerine göre **araba fren balatası** ile doğrudan eşleşen bir ürün bulunmamaktadır. Context içindeki kaynaklar; tekerlek saplaması (FEBI), helezon yay (KYB), salıncak kolu (LEMFÖRDER), debriyaj seti (LUK) ve el freni halat ayarı (DemoAuto) gibi farklı parça gruplarını içermektedir.

Ancak, "balata" kelimesi geçen ve en yüksek öneri skoruna sahip aday şudur:

*   **LUK Debriyaj Seti (Baskı Balata)**
    *   **Ürün Kodu:** CLUTCH-KIT-LUK
    *   **Marka:** LUK
    *   **Görsel:** images/clutch_kit_luk.jpg
    *   **Öneri Skoru:** 0.3797
    *   **Rating:** 4.8
    *   **Fiyat:** 7500

Diğer adaylar:
*   **FEBI Tekerlek Saplaması:** Öneri Skoru 0.4831, Rating 4.9, Fiyat 150
*   **KYB Helezon Yayı:** Öneri Skoru 0.4224, Rating 4.4, Fiyat 1450
*   **LEMFÖRDER Salıncak Kolu:** Öneri Skoru 0.4105, Rating 4.9, Fiyat 3800

Bu verilere göre en iyi fren balatası markasını kesin seçemem. Ancak context içindeki en yüksek öneri skoruna sahip ürün **FEBI**'dir (0.4831), ancak bu ürün bir tekerlek saplamasıdır. Fren balatası spesifik olarak **LUK** markalı debriyaj baskı balatası olarak geçmektedir.

Kaynaklar:
- semantic_recommendation_fallback | Tekerlek Saplaması / Bijon | WHEEL-BOLT-FEBI | images/wheel_bolt_febi.jpg
- semantic_recommendation_fallback | Helezon Yayı Ön | COIL-SPRING-KYB | images/coil_spring_kyb.jpg
- semantic_recommendation_fallback | Salıncak (Tabla) Ön Alt | CONTROL-ARM-LEM | images/control_arm_lemforder.webp
- semantic_recommendation_fallback | Debriyaj Seti (Baskı Balata) | CLUTCH-KIT-LUK | images/clutch_kit_luk.jpg
- semantic_recommendation_fallback | Park Freni (El Freni) Halat Ayarı | HANDBRAKE-ADJ | None

================================================================================
Soru: en ucuz araba yağı markası hangisi

Cevap:
Verilen bilgilere göre en ucuz araba yağı markası **Performance Plus**'tır.

**Detaylı Karşılaştırma:**

1.  **Performance Plus**
    *   **Fiyat:** 950 TL (En Düşük)
    *   **Öneri Skoru:** 0.5165
    *   **Rating:** 4.0
    *   **Yorum Sayısı:** 385
    *   **Garanti:** Bilgi yok
    *   **Ürün Kodu:** ENGINE-OIL-PPLUS
    *   **Görsel:** images/engine_oil_performance_plus_5w_20.jpg

2.  **TOTAL**
    *   **Fiyat:** 1000 TL
    *   **Öneri Skoru:** 0.555
    *   **Rating:** 4.5
    *   **Yorum Sayısı:** 400
    *   **Garanti:** Bilgi yok
    *   **Ürün Kodu:** ENGINE-OIL-TOTAL
    *   **Görsel:** images/engine_oil_total_quartz_5w_40.jpg

3.  **CASTROL**
    *   **Fiyat:** 1050 TL
    *   **Öneri Skoru:** 0.5297
    *   **Rating:** 4.2
    *   **Yorum Sayısı:** 389
    *   **Garanti:** Bilgi yok
    *   **Ürün Kodu:** ENGINE-OIL-CASTROL
    *   **Görsel:** images/engine_oil_castrol_magnetic.jpg

4.  **SHELL**
    *   **Fiyat:** 1100 TL
    *   **Öneri Skoru:** 0.534
    *   **Rating:** 4.1
    *   **Yorum Sayısı:** 430
    *   **Garanti:** Bilgi yok
    *   **Ürün Kodu:** ENGINE-OIL-SHELL
    *   **Görsel:** images/engine_oil_shell_helix_ultra_5w_40.jpeg

**Sonuç:** Fiyat kriterine göre en uygun seçenek **Performance Plus** (950 TL) iken, öneri skoru ve rating açısından **TOTAL** öne çıkmaktadır.

Kaynaklar:
- recommendation_candidates | Motor yağı görseli | ENGINE-OIL-TOTAL | images/engine_oil_total_quartz_5w_40.jpg
- recommendation_candidates | Motor yağı görseli | ENGINE-OIL-SHELL | images/engine_oil_shell_helix_ultra_5w_40.jpeg
- recommendation_candidates | Motor yağı görseli | ENGINE-OIL-CASTROL | images/engine_oil_castrol_magnetic.jpg
- recommendation_candidates | Motor yağı görseli | ENGINE-OIL-PPLUS | images/engine_oil_performance_plus_5w_20.jpg

================================================================================
Soru: fiyat performans akü öner

Cevap:
Fiyat performans kriterine göre en yüksek **recommendation_score** (0.8256) ile **POWERLINE** marka akü öne çıkmaktadır. Ancak detaylı karşılaştırma aşağıdadır:

**1. POWERLINE (BAT-12V-PWRLN)**
*   **Öneri Skoru:** 0.8256 (En Yüksek)
*   **Fiyat:** 2900 TL
*   **Garanti:** 36 Ay (En Uzun)
*   **Rating:** 4.3 / 5.0
*   **Yorum Sayısı:** 330
*   **CCA:** 670
*   **Görsel:** images/car_battery_powerline.webp

**2. BOSCH (BAT-12V-BOSCH)**
*   **Öneri Skoru:** 0.787
*   **Fiyat:** 2850 TL (En Düşük Fiyat)
*   **Garanti:** 24 Ay
*   **Rating:** 4.7 / 5.0 (En Yüksek Puan)
*   **Yorum Sayısı:** 320
*   **CCA:** 680 (En Yüksek Akım)
*   **Görsel:** images/car_battery_bosch.png

**3. EVER START (BAT-12V-VRSTRT)**
*   **Öneri Skoru:** 0.6697
*   **Fiyat:** 3100 TL (En Yüksek Fiyat)
*   **Garanti:** 12 Ay
*   **Rating:** 4.1 / 5.0
*   **Yorum Sayısı:** 322
*   **CCA:** 660
*   **Görsel:** images/car_battery_ever_start.jpeg

**Sonuç:**
Öneri skoru en yüksek olan **POWERLINE** aküsü, en uzun garanti süresi (36 ay) ve dengeli fiyatı ile fiyat-performans dengesini en iyi sağlayan seçenektir. Eğer bütçe daha kritikse ve en düşük fiyatı arıyorsanız **BOSCH** (2850 TL) tercih edilebilir; ancak POWERLINE'ın garanti avantajı daha belirgindir.

Kaynaklar:
- recommendation_candidates | Araç Aküsü Görseli | BAT-12V-PWRLN | images/car_battery_powerline.webp
- recommendation_candidates | Araç Aküsü Görseli | BAT-12V-BOSCH | images/car_battery_bosch.png
- recommendation_candidates | Araç Aküsü Görseli | BAT-12V-VRSTRT | images/car_battery_ever_start.jpeg


'''