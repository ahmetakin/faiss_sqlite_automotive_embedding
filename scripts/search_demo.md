(.llmproject_env) user@user:~/ahmet-ai/faiss_sqlite_automotive$ PYTHONPATH=. python scripts/03_search_demo.py

================================================================================
Sorgu: elektrikli araç batarya garanti süresi kaç yıl
Embedding modeli yükleniyor...
Loading weights: 100%|████████████████████████████████████████████████████| 625/625 [00:00<00:00, 675.51it/s]
Model hazır.
Model device: cuda:0

Sonuçlar:

1. Skor       : 0.8705
   Tip        : text
   Başlık     : Elektrikli Araç Batarya Garanti Politikası
   Kategori   : garanti
   Ürün kodu  : EV-BATTERY-WARRANTY
   Kaynak     : servis_dokumani
   Görsel     : None
   İçerik     : Elektrikli araç yüksek voltaj bataryaları 8 yıl veya 160.000 kilometre garanti kapsamındadır. Garanti kapsamında değerlendirilebilmesi için batarya kapasitesinin belirlenen eşik seviyenin altına düşmesi gerekir. Yetkisiz müdahale, fiziksel hasar veya uygunsuz şarj altyapısı nedeniyle oluşan arızalar garanti dışı sayılabilir.
   Metadata   : {'brand': 'DemoAuto', 'vehicle_type': 'electric', 'department': 'after_sales'}
--------------------------------------------------------------------------------
2. Skor       : 0.7772
   Tip        : text
   Başlık     : Fren Balatası Arıza Belirtileri
   Kategori   : teknik_bilgi
   Ürün kodu  : BRK-PAD-INFO
   Kaynak     : teknik_bilgi_bankasi
   Görsel     : None
   İçerik     : Fren balatası aşınması durumunda frenleme sırasında ötme sesi, fren mesafesinde uzama, pedalda sertleşme veya direksiyonda titreşim görülebilir. Balata kalınlığı kritik seviyeye düştüğünde balata değişimi yapılmalıdır.
   Metadata   : {'brand': 'DemoAuto', 'part_group': 'brake_system'}
--------------------------------------------------------------------------------
3. Skor       : 0.7716
   Tip        : text
   Başlık     : Motor Yağı Değişim Prosedürü
   Kategori   : servis
   Ürün kodu  : ENG-OIL-SERVICE
   Kaynak     : servis_proseduru
   Görsel     : None
   İçerik     : Benzinli araçlarda motor yağı değişimi normal kullanım koşullarında 10.000 kilometre veya 12 ayda bir yapılmalıdır. Ağır kullanım koşullarında bu süre 7.500 kilometreye düşürülebilir. Yağ filtresi her yağ değişiminde yenilenmelidir.
   Metadata   : {'brand': 'DemoAuto', 'part_group': 'engine'}
--------------------------------------------------------------------------------
4. Skor       : 0.4690
   Tip        : image
   Başlık     : Araç Aküsü Görseli
   Kategori   : yedek_parca_gorsel
   Ürün kodu  : BAT-12V-BOSCH
   Kaynak     : parca_gorsel_katalogu
   Görsel     : images/car_battery_bosch.png
   İçerik     : 12V araç aküsü, otomotiv marş sistemi ve elektrik besleme parçası.
   Metadata   : {'brand': 'BOSCH', 'part_group': 'battery', 'voltage': '12V'}
--------------------------------------------------------------------------------
5. Skor       : 0.4184
   Tip        : image
   Başlık     : Araç Aküsü Görseli
   Kategori   : yedek_parca_gorsel
   Ürün kodu  : BAT-12V-PWRLN
   Kaynak     : parca_gorsel_katalogu
   Görsel     : images/car_battery_powerline.webp
   İçerik     : 12V araç aküsü, otomotiv marş sistemi ve elektrik besleme parçası.
   Metadata   : {'brand': 'POWERLINE', 'part_group': 'battery', 'voltage': '12V'}
--------------------------------------------------------------------------------

================================================================================
Sorgu: araba aküsü görselini getir
Embedding modeli yükleniyor...
Loading weights: 100%|████████████████████████████████████████████████████| 625/625 [00:00<00:00, 693.80it/s]
Model hazır.
Model device: cuda:0

Sonuçlar:

1. Skor       : 0.7651
   Tip        : text
   Başlık     : Fren Balatası Arıza Belirtileri
   Kategori   : teknik_bilgi
   Ürün kodu  : BRK-PAD-INFO
   Kaynak     : teknik_bilgi_bankasi
   Görsel     : None
   İçerik     : Fren balatası aşınması durumunda frenleme sırasında ötme sesi, fren mesafesinde uzama, pedalda sertleşme veya direksiyonda titreşim görülebilir. Balata kalınlığı kritik seviyeye düştüğünde balata değişimi yapılmalıdır.
   Metadata   : {'brand': 'DemoAuto', 'part_group': 'brake_system'}
--------------------------------------------------------------------------------
2. Skor       : 0.7600
   Tip        : text
   Başlık     : Elektrikli Araç Batarya Garanti Politikası
   Kategori   : garanti
   Ürün kodu  : EV-BATTERY-WARRANTY
   Kaynak     : servis_dokumani
   Görsel     : None
   İçerik     : Elektrikli araç yüksek voltaj bataryaları 8 yıl veya 160.000 kilometre garanti kapsamındadır. Garanti kapsamında değerlendirilebilmesi için batarya kapasitesinin belirlenen eşik seviyenin altına düşmesi gerekir. Yetkisiz müdahale, fiziksel hasar veya uygunsuz şarj altyapısı nedeniyle oluşan arızalar garanti dışı sayılabilir.
   Metadata   : {'brand': 'DemoAuto', 'vehicle_type': 'electric', 'department': 'after_sales'}
--------------------------------------------------------------------------------
3. Skor       : 0.7159
   Tip        : text
   Başlık     : Motor Yağı Değişim Prosedürü
   Kategori   : servis
   Ürün kodu  : ENG-OIL-SERVICE
   Kaynak     : servis_proseduru
   Görsel     : None
   İçerik     : Benzinli araçlarda motor yağı değişimi normal kullanım koşullarında 10.000 kilometre veya 12 ayda bir yapılmalıdır. Ağır kullanım koşullarında bu süre 7.500 kilometreye düşürülebilir. Yağ filtresi her yağ değişiminde yenilenmelidir.
   Metadata   : {'brand': 'DemoAuto', 'part_group': 'engine'}
--------------------------------------------------------------------------------
4. Skor       : 0.4048
   Tip        : image
   Başlık     : Araç Aküsü Görseli
   Kategori   : yedek_parca_gorsel
   Ürün kodu  : BAT-12V-BOSCH
   Kaynak     : parca_gorsel_katalogu
   Görsel     : images/car_battery_bosch.png
   İçerik     : 12V araç aküsü, otomotiv marş sistemi ve elektrik besleme parçası.
   Metadata   : {'brand': 'BOSCH', 'part_group': 'battery', 'voltage': '12V'}
--------------------------------------------------------------------------------
5. Skor       : 0.3794
   Tip        : image
   Başlık     : Fren Balatası Görseli
   Kategori   : yedek_parca_gorsel
   Ürün kodu  : BRK-PAD-FRONT-SBS-FC5
   Kaynak     : parca_gorsel_katalogu
   Görsel     : images/brake_pad_sbs_honda_civic_fc5_front.jpg
   İçerik     : Ön fren balatası, disk fren sistemi için kullanılan yedek parça. Honda civic fc5 kasa uyumlu.
   Metadata   : {'brand': 'SBS', 'part_group': 'brake_system'}
--------------------------------------------------------------------------------

================================================================================
Sorgu: fren balatası aşınırsa ne olur
Embedding modeli yükleniyor...
Loading weights: 100%|████████████████████████████████████████████████████| 625/625 [00:00<00:00, 714.18it/s]
Model hazır.
Model device: cuda:0

Sonuçlar:

1. Skor       : 0.7939
   Tip        : text
   Başlık     : Fren Balatası Arıza Belirtileri
   Kategori   : teknik_bilgi
   Ürün kodu  : BRK-PAD-INFO
   Kaynak     : teknik_bilgi_bankasi
   Görsel     : None
   İçerik     : Fren balatası aşınması durumunda frenleme sırasında ötme sesi, fren mesafesinde uzama, pedalda sertleşme veya direksiyonda titreşim görülebilir. Balata kalınlığı kritik seviyeye düştüğünde balata değişimi yapılmalıdır.
   Metadata   : {'brand': 'DemoAuto', 'part_group': 'brake_system'}
--------------------------------------------------------------------------------
2. Skor       : 0.7292
   Tip        : text
   Başlık     : Elektrikli Araç Batarya Garanti Politikası
   Kategori   : garanti
   Ürün kodu  : EV-BATTERY-WARRANTY
   Kaynak     : servis_dokumani
   Görsel     : None
   İçerik     : Elektrikli araç yüksek voltaj bataryaları 8 yıl veya 160.000 kilometre garanti kapsamındadır. Garanti kapsamında değerlendirilebilmesi için batarya kapasitesinin belirlenen eşik seviyenin altına düşmesi gerekir. Yetkisiz müdahale, fiziksel hasar veya uygunsuz şarj altyapısı nedeniyle oluşan arızalar garanti dışı sayılabilir.
   Metadata   : {'brand': 'DemoAuto', 'vehicle_type': 'electric', 'department': 'after_sales'}
--------------------------------------------------------------------------------
3. Skor       : 0.6918
   Tip        : text
   Başlık     : Motor Yağı Değişim Prosedürü
   Kategori   : servis
   Ürün kodu  : ENG-OIL-SERVICE
   Kaynak     : servis_proseduru
   Görsel     : None
   İçerik     : Benzinli araçlarda motor yağı değişimi normal kullanım koşullarında 10.000 kilometre veya 12 ayda bir yapılmalıdır. Ağır kullanım koşullarında bu süre 7.500 kilometreye düşürülebilir. Yağ filtresi her yağ değişiminde yenilenmelidir.
   Metadata   : {'brand': 'DemoAuto', 'part_group': 'engine'}
--------------------------------------------------------------------------------
4. Skor       : 0.3509
   Tip        : image
   Başlık     : Fren Balatası Görseli
   Kategori   : yedek_parca_gorsel
   Ürün kodu  : BRK-PAD-FRONT-SBS-FC5
   Kaynak     : parca_gorsel_katalogu
   Görsel     : images/brake_pad_sbs_honda_civic_fc5_front.jpg
   İçerik     : Ön fren balatası, disk fren sistemi için kullanılan yedek parça. Honda civic fc5 kasa uyumlu.
   Metadata   : {'brand': 'SBS', 'part_group': 'brake_system'}
--------------------------------------------------------------------------------
5. Skor       : 0.3379
   Tip        : image
   Başlık     : Araç Aküsü Görseli
   Kategori   : yedek_parca_gorsel
   Ürün kodu  : BAT-12V-BOSCH
   Kaynak     : parca_gorsel_katalogu
   Görsel     : images/car_battery_bosch.png
   İçerik     : 12V araç aküsü, otomotiv marş sistemi ve elektrik besleme parçası.
   Metadata   : {'brand': 'BOSCH', 'part_group': 'battery', 'voltage': '12V'}
--------------------------------------------------------------------------------

================================================================================
Sorgu: motor yağı kaç kilometrede değişir
Embedding modeli yükleniyor...
Loading weights: 100%|████████████████████████████████████████████████████| 625/625 [00:00<00:00, 781.72it/s]
Model hazır.
Model device: cuda:0

Sonuçlar:

1. Skor       : 0.7728
   Tip        : text
   Başlık     : Motor Yağı Değişim Prosedürü
   Kategori   : servis
   Ürün kodu  : ENG-OIL-SERVICE
   Kaynak     : servis_proseduru
   Görsel     : None
   İçerik     : Benzinli araçlarda motor yağı değişimi normal kullanım koşullarında 10.000 kilometre veya 12 ayda bir yapılmalıdır. Ağır kullanım koşullarında bu süre 7.500 kilometreye düşürülebilir. Yağ filtresi her yağ değişiminde yenilenmelidir.
   Metadata   : {'brand': 'DemoAuto', 'part_group': 'engine'}
--------------------------------------------------------------------------------
2. Skor       : 0.7554
   Tip        : text
   Başlık     : Fren Balatası Arıza Belirtileri
   Kategori   : teknik_bilgi
   Ürün kodu  : BRK-PAD-INFO
   Kaynak     : teknik_bilgi_bankasi
   Görsel     : None
   İçerik     : Fren balatası aşınması durumunda frenleme sırasında ötme sesi, fren mesafesinde uzama, pedalda sertleşme veya direksiyonda titreşim görülebilir. Balata kalınlığı kritik seviyeye düştüğünde balata değişimi yapılmalıdır.
   Metadata   : {'brand': 'DemoAuto', 'part_group': 'brake_system'}
--------------------------------------------------------------------------------
3. Skor       : 0.7389
   Tip        : text
   Başlık     : Elektrikli Araç Batarya Garanti Politikası
   Kategori   : garanti
   Ürün kodu  : EV-BATTERY-WARRANTY
   Kaynak     : servis_dokumani
   Görsel     : None
   İçerik     : Elektrikli araç yüksek voltaj bataryaları 8 yıl veya 160.000 kilometre garanti kapsamındadır. Garanti kapsamında değerlendirilebilmesi için batarya kapasitesinin belirlenen eşik seviyenin altına düşmesi gerekir. Yetkisiz müdahale, fiziksel hasar veya uygunsuz şarj altyapısı nedeniyle oluşan arızalar garanti dışı sayılabilir.
   Metadata   : {'brand': 'DemoAuto', 'vehicle_type': 'electric', 'department': 'after_sales'}
--------------------------------------------------------------------------------
4. Skor       : 0.3864
   Tip        : image
   Başlık     : Fren Balatası Görseli
   Kategori   : yedek_parca_gorsel
   Ürün kodu  : BRK-PAD-FRONT-SBS-FC5
   Kaynak     : parca_gorsel_katalogu
   Görsel     : images/brake_pad_sbs_honda_civic_fc5_front.jpg
   İçerik     : Ön fren balatası, disk fren sistemi için kullanılan yedek parça. Honda civic fc5 kasa uyumlu.
   Metadata   : {'brand': 'SBS', 'part_group': 'brake_system'}
--------------------------------------------------------------------------------
5. Skor       : 0.3837
   Tip        : image
   Başlık     : Araç Aküsü Görseli
   Kategori   : yedek_parca_gorsel
   Ürün kodu  : BAT-12V-BOSCH
   Kaynak     : parca_gorsel_katalogu
   Görsel     : images/car_battery_bosch.png
   İçerik     : 12V araç aküsü, otomotiv marş sistemi ve elektrik besleme parçası.
   Metadata   : {'brand': 'BOSCH', 'part_group': 'battery', 'voltage': '12V'}
--------------------------------------------------------------------------------

================================================================================
Sorgu: ENGINE-OIL-CASTROL ürün kodlu parça
Embedding modeli yükleniyor...
Loading weights: 100%|████████████████████████████████████████████████████| 625/625 [00:00<00:00, 677.18it/s]
Model hazır.
Model device: cuda:0

Sonuçlar:

1. Skor       : 0.7297
   Tip        : text
   Başlık     : Motor Yağı Değişim Prosedürü
   Kategori   : servis
   Ürün kodu  : ENG-OIL-SERVICE
   Kaynak     : servis_proseduru
   Görsel     : None
   İçerik     : Benzinli araçlarda motor yağı değişimi normal kullanım koşullarında 10.000 kilometre veya 12 ayda bir yapılmalıdır. Ağır kullanım koşullarında bu süre 7.500 kilometreye düşürülebilir. Yağ filtresi her yağ değişiminde yenilenmelidir.
   Metadata   : {'brand': 'DemoAuto', 'part_group': 'engine'}
--------------------------------------------------------------------------------
2. Skor       : 0.7016
   Tip        : text
   Başlık     : Fren Balatası Arıza Belirtileri
   Kategori   : teknik_bilgi
   Ürün kodu  : BRK-PAD-INFO
   Kaynak     : teknik_bilgi_bankasi
   Görsel     : None
   İçerik     : Fren balatası aşınması durumunda frenleme sırasında ötme sesi, fren mesafesinde uzama, pedalda sertleşme veya direksiyonda titreşim görülebilir. Balata kalınlığı kritik seviyeye düştüğünde balata değişimi yapılmalıdır.
   Metadata   : {'brand': 'DemoAuto', 'part_group': 'brake_system'}
--------------------------------------------------------------------------------
3. Skor       : 0.6708
   Tip        : text
   Başlık     : Elektrikli Araç Batarya Garanti Politikası
   Kategori   : garanti
   Ürün kodu  : EV-BATTERY-WARRANTY
   Kaynak     : servis_dokumani
   Görsel     : None
   İçerik     : Elektrikli araç yüksek voltaj bataryaları 8 yıl veya 160.000 kilometre garanti kapsamındadır. Garanti kapsamında değerlendirilebilmesi için batarya kapasitesinin belirlenen eşik seviyenin altına düşmesi gerekir. Yetkisiz müdahale, fiziksel hasar veya uygunsuz şarj altyapısı nedeniyle oluşan arızalar garanti dışı sayılabilir.
   Metadata   : {'brand': 'DemoAuto', 'vehicle_type': 'electric', 'department': 'after_sales'}
--------------------------------------------------------------------------------
4. Skor       : 0.4494
   Tip        : image
   Başlık     : Fren Balatası Görseli
   Kategori   : yedek_parca_gorsel
   Ürün kodu  : BRK-PAD-FRONT-SBS-FC5
   Kaynak     : parca_gorsel_katalogu
   Görsel     : images/brake_pad_sbs_honda_civic_fc5_front.jpg
   İçerik     : Ön fren balatası, disk fren sistemi için kullanılan yedek parça. Honda civic fc5 kasa uyumlu.
   Metadata   : {'brand': 'SBS', 'part_group': 'brake_system'}
--------------------------------------------------------------------------------
5. Skor       : 0.4123
   Tip        : image
   Başlık     : Araç Aküsü Görseli
   Kategori   : yedek_parca_gorsel
   Ürün kodu  : BAT-12V-BOSCH
   Kaynak     : parca_gorsel_katalogu
   Görsel     : images/car_battery_bosch.png
   İçerik     : 12V araç aküsü, otomotiv marş sistemi ve elektrik besleme parçası.
   Metadata   : {'brand': 'BOSCH', 'part_group': 'battery', 'voltage': '12V'}
--------------------------------------------------------------------------------
(.llmproject_env) user@user:~/ahmet-ai/faiss_sqlite_automotive$
