# EDA Çıktı Örnekleri - Adım Adım Rehber

Bu dokümantasyon, her EDA adımında ne tür çıktılar beklenmesi gerektiğini ve bu çıktıların nasıl yorumlanacağını açıklar.

## 📋 İçindekiler

1. [Veri Seti Genel Bakış Çıktıları](#1-veri-seti-genel-bakış-çıktıları)
2. [Kategorik Değişken Analizi Çıktıları](#2-kategorik-değişken-analizi-çıktıları)
3. [Target Variable Profiling Çıktıları](#3-target-variable-profiling-çıktıları)
4. [YData Profiling Raporu Çıktıları](#4-ydata-profiling-raporu-çıktıları)

---

## 1. Veri Seti Genel Bakış Çıktıları

### 1.1 Dataset Shape
```
Number of rows: 32,561
Number of columns: 15
Total cells: 488,415
```
**Yorumlama**: Veri setinin boyutunu gösterir. Bu bilgi, veri setinin büyüklüğünü ve analiz için yeterli olup olmadığını değerlendirmemize yardımcı olur.

### 1.2 Data Types
```
age                int64
workclass         object
fnlwgt             int64
education         object
...
```
**Yorumlama**: Her sütunun veri tipini gösterir. Sayısal (int64, float64) ve kategorik (object) değişkenleri ayırt etmemize yardımcı olur.

### 1.3 Missing Values Analysis
```
Columns with missing values:
Column          Missing Count  Missing Percentage
occupation           1843                   5.66
workclass            1836                   5.63
native.country        583                   1.79

Total missing cells: 4,262
Total missing percentage: 0.87%
```
**Yorumlama**: 
- Hangi sütunlarda eksik değer olduğunu gösterir
- Eksik değer yüzdesi %5'in üzerindeyse dikkat edilmelidir
- Eksik değer stratejisi belirlenmelidir (silme, doldurma, vb.)

### 1.4 Duplicate Rows
```
Number of duplicate rows: 24
Duplicate percentage: 0.07%
```
**Yorumlama**: 
- Tekrar eden kayıt sayısını gösterir
- Yüksek duplicate oranı veri kalitesi sorununu işaret edebilir
- Genellikle %1'in altı kabul edilebilir

### 1.5 Basic Statistics (Numerical Columns)
```
              age      fnlwgt  education.num  capital.gain  capital.loss  hours.per.week
count  32561.0000  32561.0000    32561.0000    32561.0000   32561.0000     32561.0000
mean      38.5816  189778.3665       10.0807     1077.6488     87.3038        40.4375
std       13.6405  105549.9777        2.5727     7385.2921    402.9602        12.3474
min       17.0000   12285.0000        1.0000        0.0000      0.0000         1.0000
25%       28.0000  117827.0000        9.0000        0.0000      0.0000        40.0000
50%       37.0000  178356.0000       10.0000        0.0000      0.0000        40.0000
75%       48.0000  237051.0000       12.0000        0.0000      0.0000        45.0000
max       90.0000  1484705.0000      16.0000    99999.0000   4356.0000        99.0000
```
**Yorumlama**:
- **count**: Eksik değer olmayan gözlem sayısı
- **mean**: Ortalama değer
- **std**: Standart sapma (değişkenlik ölçüsü)
- **min/max**: Minimum ve maksimum değerler
- **25%, 50%, 75%**: Quartile'lar (medyan = 50%)

---

## 2. Kategorik Değişken Analizi Çıktıları

### 2.1 Value Counts
```
1. WORKCLASS
Value counts:
Private             22696
Self-emp-not-inc     2541
Local-gov            2093
State-gov            1298
Self-emp-inc         1116
Federal-gov           960
Without-pay            14
Never-worked            7

Value counts (%):
Private: 22,696 (69.70%)
Self-emp-not-inc: 2,541 (7.80%)
...
```
**Yorumlama**:
- Her kategorinin frekansını gösterir
- Kategori dağılımının dengeli olup olmadığını kontrol ederiz
- Çok düşük frekanslı kategoriler (rare categories) dikkat gerektirir

### 2.2 Statistics
```
Statistics:
  Unique values: 8
  Missing values: 1836 (5.63%)
  Most frequent: Private
```
**Yorumlama**:
- **Unique values**: Kategori sayısı (yüksekse encoding zorlaşabilir)
- **Missing values**: Eksik değer sayısı ve yüzdesi
- **Most frequent**: En sık görülen kategori (mod)

---

## 3. Target Variable Profiling Çıktıları

### 3.1 Target Variable Distribution
```
1. TARGET VARIABLE DISTRIBUTION
income Distribution:
<=50K    24720
>50K      7841

income Distribution (%):
<=50K    75.92%
>50K     24.08%
```
**Yorumlama**:
- **Class Imbalance**: Target variable'da dengesizlik var mı?
- Bu örnekte %75.92 vs %24.08 → **Imbalanced dataset**
- Model eğitiminde bu durumu dikkate almak gerekir (SMOTE, class weights, vb.)

### 3.2 Numerical Features vs Target
```
age:
        <=50K        >50K
count  24720.0    7841.0
mean     36.78     44.25
std      14.02     10.52
min      17.00     19.00
25%      25.00     36.00
50%      34.00     43.00
75%      46.00     52.00
max      90.00     90.00

T-test p-value: 0.000000 (Significant)
```
**Yorumlama**:
- Her gelir grubu için sayısal özelliklerin istatistiksel özeti
- **T-test**: İki grup arasında anlamlı fark var mı?
  - p-value < 0.05 → **Significant** (gruplar arası fark anlamlı)
  - p-value >= 0.05 → **Not Significant** (gruplar arası fark anlamlı değil)
- Bu örnekte yaş ile gelir arasında anlamlı bir fark var (yüksek gelirli grup daha yaşlı)

### 3.3 Categorical Features vs Target
```
relationship:
Count:
                <=50K   >50K  All
Husband          13193   6662  19855
Not-in-family     8305    981   9286
Own-child         5068     76   5144
Unmarried         3446    410   3856
Wife              1568   1128   2696
Other-relative     981     64   1045
All              24720   7841  32561

Percentage (%):
                <=50K      >50K
Husband         66.48    84.96
Not-in-family   89.43    10.57
Own-child       98.52     1.48
...

Chi-square test p-value: 0.000000 (Significant)
```
**Yorumlama**:
- **Cross-tabulation**: Her kategori için gelir dağılımı
- **Percentage**: Her kategoride yüksek/düşük gelirli oranı
  - Örnek: "Husband" kategorisinde %84.96 yüksek gelirli
- **Chi-square test**: Kategorik değişken ile target arasında ilişki var mı?
  - p-value < 0.05 → **Significant** (ilişki var)
  - Bu örnekte relationship ile income arasında güçlü bir ilişki var

### 3.4 Feature Importance Ranking
```
TOP FEATURES BY IMPORTANCE (Combined Ranking):
1. relationship: 0.4523
2. marital.status: 0.4121
3. age: 0.2345
4. education.num: 0.2234
5. hours.per.week: 0.1987
6. capital.gain: 0.1543
7. occupation: 0.1421
8. sex: 0.1234
9. workclass: 0.0987
10. race: 0.0456
```
**Yorumlama**:
- **Sayısal özellikler**: Korelasyon katsayısı (0 ile 1 arası, mutlak değer)
- **Kategorik özellikler**: Cramér's V (0 ile 1 arası)
- **Yorumlama**:
  - 0.0 - 0.1: Çok zayıf ilişki
  - 0.1 - 0.3: Zayıf ilişki
  - 0.3 - 0.5: Orta ilişki
  - 0.5 - 0.7: Güçlü ilişki
  - 0.7 - 1.0: Çok güçlü ilişki
- Bu örnekte "relationship" ve "marital.status" en önemli özellikler

### 3.5 Key Insights
```
En yüksek anlam içeren değişkenler (Target ile güçlü ilişki):
  - relationship: 0.4523
  - marital.status: 0.4121
  - age: 0.2345
  - education.num: 0.2234
  - hours.per.week: 0.1987
```
**Yorumlama**:
- Model eğitimi için en önemli özellikler
- Feature selection yaparken bu listeyi kullanabiliriz
- Düşük önemli özellikler (örn: race: 0.0456) modelden çıkarılabilir

---

## 4. YData Profiling Raporu Çıktıları

### 4.1 HTML Raporu Yapısı

YData Profiling, `adult_report.html` adında interaktif bir HTML raporu oluşturur.

#### 4.1.1 Overview Section
- **Dataset info**: Satır/sütun sayısı, eksik değer yüzdesi
- **Variables**: Değişken sayısı (sayısal/kategorik)
- **Warnings**: Veri kalitesi uyarıları

#### 4.1.2 Variables Section
Her değişken için:
- **Statistics**: Temel istatistikler
- **Histogram**: Dağılım grafiği
- **Common values**: En sık görülen değerler
- **Extreme values**: Aykırı değerler

#### 4.1.3 Interactions Section
- **Scatter plots**: Sayısal değişkenler arası ilişkiler
- **Correlation matrix**: Korelasyon matrisi

#### 4.1.4 Correlations Section
- **Pearson correlation**: Sayısal değişkenler için
- **Spearman correlation**: Sıralı değişkenler için
- **Kendall correlation**: Küçük veri setleri için
- **Cramér's V**: Kategorik değişkenler için

#### 4.1.5 Missing Values Section
- **Missing values matrix**: Eksik değerlerin görselleştirmesi
- **Missing values heatmap**: Eksik değerlerin korelasyonu

#### 4.1.6 Sample Section
- **First rows**: İlk 10 satır
- **Last rows**: Son 10 satır

### 4.2 Raporu Yorumlama

1. **Overview'a bakın**: Genel veri kalitesi nasıl?
2. **Warnings'leri kontrol edin**: Hangi uyarılar var?
3. **Correlations'a odaklanın**: Hangi özellikler birbiriyle ilişkili?
4. **Missing values'i inceleyin**: Eksik değerler rastgele mi yoksa pattern var mı?
5. **Interactions'ı keşfedin**: Beklenmedik ilişkiler var mı?

---

## 📊 Genel EDA Çıktı Kontrol Listesi

Her EDA çalışmasında şunları kontrol edin:

- [ ] Veri seti boyutu ve yapısı anlaşıldı mı?
- [ ] Eksik değerler tespit edildi ve strateji belirlendi mi?
- [ ] Duplicate kayıtlar kontrol edildi mi?
- [ ] Sayısal değişkenlerin dağılımı incelendi mi?
- [ ] Kategorik değişkenlerin frekansları analiz edildi mi?
- [ ] Target variable dağılımı kontrol edildi mi? (Class imbalance?)
- [ ] Her özellik için target ile ilişki analiz edildi mi?
- [ ] Feature importance sıralaması yapıldı mı?
- [ ] Korelasyon matrisi incelendi mi? (Multicollinearity?)
- [ ] Aykırı değerler (outliers) tespit edildi mi?
- [ ] Görselleştirmeler oluşturuldu mu?
- [ ] Key insights özetlendi mi?

---

## 🎯 Sonraki Adımlar

EDA tamamlandıktan sonra:

1. **Data Preprocessing**: Eksik değer doldurma, encoding, scaling
2. **Feature Engineering**: Yeni özellikler oluşturma
3. **Feature Selection**: Önemli özellikleri seçme
4. **Model Training**: Makine öğrenmesi modelleri eğitme
5. **Model Evaluation**: Model performansını değerlendirme

---

## 📚 Kaynaklar

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [YData Profiling Documentation](https://ydata-profiling.ydata.ai/)
- [Statistical Tests Guide](https://www.statstest.com/)

