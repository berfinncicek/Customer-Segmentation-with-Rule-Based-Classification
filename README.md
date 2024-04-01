## Müşteri Segmentasyonu ve Tahmini

Bu proje, bir oyun şirketinin müşteri verileri üzerinde analizler yaparak yeni müşteri segmentlerini ve bu segmentlere göre ortalama gelir tahminlerini oluşturmayı amaçlamaktadır. Veri seti, şirketin sattığı ürünlerin fiyatları ve bu ürünleri satın alan kullanıcıların bazı demografik bilgilerini içermektedir.

### Veri Yükleme ve İnceleme

- Veri seti load_data fonksiyonu ile yüklenir.
- check_df fonksiyonu ile veri setinin genel yapısal incelemesi yapılır: boyutlar, veri tipleri, ilk ve son 5 gözlem, eksik veri kontrolü ve temel istatistikler.

### Demografik Özelliklerin Frekansları

- calculate_column_unique_frequencies fonksiyonu ile her demografik özelliğin benzersiz değerlerinin ve frekanslarının hesaplanması yapılır.
- Örnek olarak: SEX sütununda kaç farklı cinsiyet var ve her bir cinsiyetten kaç tane gözlem var gibi.

### Ülkelere Göre Toplam Satış ve Müşteri Sayısı

- sales_by_country ile ülkelere göre toplam satış ve müşteri sayısı hesaplanır.

### Ülke ve Platforma Göre Ortalama Fiyatlar

- avg_prices_by_country_source ile ülke ve platforma göre ortalama satış fiyatları hesaplanır.

### Demografik Özellikler ve Yaşa Göre Ortalama Fiyatlar

- avg_prices_by_segment_sorted ile ülke, platform, cinsiyet ve yaşa göre ortalama satış fiyatları hesaplanır ve sıralanır.
### Yaş Kategorilerine Göre Segmentasyon

- Müşteriler yaş kategorilerine göre segmentlere ayrılır: 0-18, 19-23, 24-30, 31-40, 41+.
- customers_level_based adında yeni bir sütun oluşturulur: "Ülke_Platform_Cinsiyet_YaşKategori".

### Segmentlere Göre Ortalama Fiyatlar ve Segmentasyon

- Segmentlere göre ortalama fiyatlar hesaplanır ve müşteri segmentleri oluşturulur.
- Elde edilen segmentlerin her birine bir harf atanır (D, C, B, A).

### Yeni Kullanıcılar İçin Segment Tahmini

- Son olarak, veri setinde olmayan yeni müşterilerin potansiyel gelirlerini tahmin etmek için oluşturulan segmentler kullanılır. Örneğin, yeni bir müşteri geldiğinde, bu müşterinin demografik bilgilerine ve satın alma alışkanlıklarına bakarak hangi segmente ait olduğu belirlenir ve bu segmentin ortalama geliri üzerinden tahmin yapılır.


Tüm bu işlemler şirketin mevcut müşterileri hakkında daha fazla anlayış kazanmasına ve potansiyel yeni müşterilerin ne kadar gelir getirebileceğini tahmin etmesine yardımcı olur. Bu bilgiler, pazarlama stratejilerini belirlemede ve kaynakları doğru bir şekilde yönlendirmede önemli bir rol oynar.
