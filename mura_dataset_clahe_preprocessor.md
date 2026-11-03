# MURA Dataset CLAHE Preprocessor

Bu proje, özellikle **MURA-v1.1** (Musculoskeletal Radiographs) gibi büyük ve karmaşık klasör yapılarına sahip tıbbi görüntü veri setlerini ön işlemek (preprocess) için geliştirilmiş bir Python betiğidir. 

Script, veri setindeki tüm görüntüleri otomatik olarak tarar, gri seviyeye (grayscale) çevirir ve **CLAHE (Contrast Limited Adaptive Histogram Equalization)** uygulayarak kontrastlarını artırır. En önemli özelliği, orijinal veri setinin alt klasör yapısını bozmadan işlenmiş görüntüleri yeni bir dizine kopyalamasıdır.

## 🚀 Özellikler

* **Toplu İşlem (Batch Processing):** Belirtilen ana dizin altındaki tüm `.png`, `.jpg` ve `.jpeg` uzantılı dosyaları otomatik bulur.
* **Klasör Yapısını Koruma:** Orijinal `MURA-v1.1` veri setindeki karmaşık klasör ağacını (hasta/çalışma/görüntü hiyerarşisini) hedef dizinde aynen yeniden oluşturur.
* **Gelişmiş Kontrast (CLAHE):** Klasik histogram eşitlemenin aksine, CLAHE algoritması kullanarak bölgesel kontrastı artırır ve aşırı parlama gürültülerini (noise) engeller.
* **Güvenli Dışa Aktarım:** İşlenmiş görüntüleri orijinal dosyaların üzerine yazmak yerine kullanıcının Masaüstünde (Desktop) `output_images` adında yeni bir klasör oluşturarak oraya kaydeder.

## 🛠️ Gereksinimler

Bu betiği çalıştırmak için sisteminizde Python yüklü olmalı ve aşağıdaki kütüphaneler kurulmalıdır:

```bash
pip install opencv-python
```
*(Not: `os` modülü Python'un standart kütüphanesine dahildir, haricen kurulmasına gerek yoktur.)*

## 📁 Dizin Yapısı ve Kurulum

Betiğin doğru çalışması için `MURA-v1.1` klasörünün Python dosyanız (örneğin `main.py`) ile **aynı dizinde** (root) bulunması gerekmektedir.

```text
PROJE_KLASORU/
│
├── main.py                # Çalıştırılacak Python dosyanız
└── MURA-v1.1/             # Orijinal veri seti klasörü
    ├── train/
    │   ├── XR_ELBOW/
    │   └── ...
    └── valid/
        └── ...
```

## 💻 Kullanım

1. `MURA-v1.1` veri setini betiğin bulunduğu dizine yerleştirin.
2. Terminal veya komut satırını açıp betiği çalıştırın:

```bash
python main.py
```

**Sonuç:** Kod çalışmayı tamamladığında, bilgisayarınızın Masaüstünde `output_images` adında bir klasör belirecek ve içinde MURA veri setinin CLAHE uygulanmış halleri, orijinal klasör hiyerarşisiyle yer alacaktır.

## 🧠 Teknik Detaylar (CLAHE Parametreleri)

Kod içerisinde OpenCV'nin `createCLAHE` fonksiyonu aşağıdaki parametrelerle kullanılmıştır:
* `clipLimit=5`: Kontrast artırma sınırını belirler. Gürültüyü sınırlamak için kullanılır.
* `tileGridSize=(8, 8)`: Görüntüyü 8x8'lik ızgaralara bölerek her bir bölge için lokal histogram eşitlemesi yapar. Bu sayede homojen olmayan aydınlatma koşulları düzeltilir.