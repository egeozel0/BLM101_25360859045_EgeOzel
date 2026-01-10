# BLM101_25360859045_EgeOzel
# Proje Konusu: Veri Depolama ve Sayısal Sistemler

## Öğrenci Bilgileri
* **Ad Soyad**: Ege Özel
* **Öğrenci No:** 25360859045

## Proje Sunum Videosu
Proje anlatım ve kod çalıştırma videosuna aşağıdaki linkten ulaşabilirsiniz:
[YouTube Video Linki](https://youtube.com/...) 

## Proje Açıklaması
### 1. Kodun İşlevi
### 1. Kodun İşlevi ve Amacı
Bu proje, kullanıcıdan onluk (decimal) tabanda alınan bir tamsayıyı, Python'un hazır fonksiyonları olan `bin()` veya `hex()` fonksiyonlarını **kullanmadan**, tamamen matematiksel algoritmalarla İkilik (Binary) veya Onaltılık (Hexadecimal) sistemlere dönüştüren bir hesaplama aracıdır.

Program ayrıca, girilen sayının bilgisayar belleğinde (memory) nasıl tutulduğunu simüle etmek amacıyla, sayıyı 8-bitlik kutucuklar halinde görselleştirerek konsola yazdırır. Negatif sayıların temsili için "Two's Complement" (İkiye Tümleme) mantığı esas alınmıştır.

### 2. Kullanılan Kütüphaneler 
Bu proje standart Python kütüphaneleri ile yazılmıştır, çalıştırılması için harici bir kütüphane kurulumu gerektirmez.


### 3. Algoritma Mantığı ve Kodun Çalışma Prensibi
Kodun çalışma mantığı şu adımlardan oluşur:

* **Girdi Alma:** Program kullanıcıdan dönüştürmek istediği onluk tabandaki sayıyı alır ve hangi tabana (Binary/Hex) dönüştürmek istediğini sorar.
* **Dönüşüm Algoritması (Hazır Fonksiyonsuz):**
    * Dönüşüm işlemi için klasik "Bölme ve Mod Alma" yöntemi kullanılmıştır.
    * Sayı, istenen tabana (2 veya 16) sürekli bölünür.
    * Her bölme işleminden kalan sayı, o basamağın değerini oluşturur.
    * Bölüm 0 olana kadar işlem bir döngü içinde devam eder ve kalanlar tersten dizilir.
* **Bellek Görselleştirme (8-Bit):**
    * Elde edilen bit dizisi, bellekteki görünümü temsil etmek üzere başına sıfırlar eklenerek 8 bite tamamlanır.
    * Görselliği artırmak için çıktılar kutucuklar (`[0] [1] ...`) formatında ekrana basılır.
* **Negatif Sayılar:**
    * Eğer girilen sayı negatif ise, Two's Complement (İkiye Tümleme) yöntemi uygulanır.
    * Sayının pozitif halinin bitleri ters çevrilir (NOT işlemi) ve sonuca 1 eklenerek bellekteki negatif karşılığı bulunur.
