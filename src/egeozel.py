import time

# -------------------------------------------------------------------------
# ÖĞRENCİ BİLGİLERİ
# Ad Soyad: Ege Özel
# Öğrenci No: 25360859045
# Proje Konusu: Sayısal Sistemler ve Veri Depolama (Taban Dönüştürücü)
# -------------------------------------------------------------------------

def onluktan_ikiliye(sayi):
    """
    Bu fonksiyon, girilen onluk (decimal) sayıyı matematiksel işlemlerle
    ikilik (binary) tabana çevirir. bin() fonksiyonu kullanılmamıştır.
    """

    if sayi == 0:
        return "0"
    
    # Negatif sayı kontrolü (8-bit Two's Complement mantığı)
    # Eğer sayı negatifse, 2^8 (256) ile toplayarak bit karşılığını buluyoruz.
    if sayi < 0: 
        sayi = 256 + sayi

    ikilik_dizi = ""
    gecici_sayi = sayi

    # Bölme ve Mod Algoritması
    while gecici_sayi > 0:
        kalan = gecici_sayi % 2  # 2'ye bölümden kalanı alır. (0 veya 1)
        ikilik_dizi = str(kalan) + ikilik_dizi  # Kalanı sonucun başına ekler
        gecici_sayi = gecici_sayi // 2  # Sayıyı 2'ye böl (tam sayı kısmı.)
        
    return ikilik_dizi

def onluktan_onaltiliga(sayi):
    """
    Bu fonksiyon, girilen onluk sayıyı onaltılık (hexadecimal) tabana çevirir.
    hex() fonksiyonu kullanılmamıştır.
    """
    if sayi == 0:
        return "0"
    
    # Negatif sayılar için 8-bit sınırlaması yapılır (Two's Complement)
    if sayi < 0:
        sayi = 256 + sayi

    hex_karakterler = "0123456789ABCDEF"
    onaltilik_dizi = ""
    gecici_sayi = sayi

    while gecici_sayi > 0:
        kalan = gecici_sayi % 16  # 16'ya bölümden kalanı buluruz.
        # Kalan sayı (örn 10) ise bunu harfe (A) çevirmek için diziyi kullanacağız.
        onaltilik_dizi = hex_karakterler[kalan] + onaltilik_dizi
        gecici_sayi = gecici_sayi // 16 # Sayıyı 16'ya böl(tam sayı bolmesi.)

    return onaltilik_dizi

def bellek_gorsellestir(binary_str):
    """Elde edilen binary dizisini 8-bite tamamlar ve kutucuklar halinde gösterir.
"""
    # 8 bit olması için başına sıfır ekleme (Padding)
    uzunluk = len(binary_str)
    if uzunluk < 8:
        binary_str = "0" * (8 - uzunluk) + binary_str
    
    # Görselleştirme (Kutucuk çizimi)
    gorsel_cikti = ""
    print("\n--- Bellek Görünümü (8-Bit) ---")
    for bit in binary_str:
        gorsel_cikti += f"[{bit}]"
    
    print(gorsel_cikti)
    print("-" * 30)

def ana_program():
    print("******************************************")
    print("   ÇOK FONKSİYONLU TABAN DÖNÜŞTÜRÜCÜ")
    print("******************************************")
    
    while True:
        try:
            print("\nLütfen bir işlem seçiniz:")
            print("1. Onluk Sayıyı İkiliye (Binary) Çevir")
            print("2. Onluk Sayıyı Onaltılığa (Hex) Çevir")
            print("3. Çıkış")
            
            secim = input("Seçiminiz (1-3): ")
            
            if secim == '3':
                print("Programdan çıkılıyor...")
                break
                
            if secim not in ['1', '2']:
                print("Hatalı seçim! Lütfen tekrar deneyin.")
                continue

            # Kullanıcıdan sayı alınır
            girilen = int(input("Dönüştürülecek onluk (decimal) sayıyı girin (-128 ile 127 arası): "))
            
            # 8-bit simülasyonu için sınır uyarısı
            if girilen > 127 or girilen < -128:
                print("UYARI: Bu program 8-bit bellek simülasyonu yapar.")
                print("Girdiğiniz sayı 8 bit sınırlarını aşıyor, sonuç hatalı görünebilir!")

            if secim == '1':
                sonuc = onluktan_ikiliye(girilen)
                print(f"\nSonuç (Binary): {sonuc}")
                # Görselleştirme için binary sonucunu kullanıyoruz
                bellek_gorsellestir(sonuc)
                
            elif secim == '2':
                sonuc_hex = onluktan_onaltiliga(girilen)
                sonuc_bin = onluktan_ikiliye(girilen) # Görselleştirme için yine binary lazım
                print(f"\nSonuç (Hexadecimal): {sonuc_hex}")
                bellek_gorsellestir(sonuc_bin) # Bellekte daima 0 ve 1 tutulur
                
        except ValueError:
            print("HATA: Lütfen geçerli bir tamsayı giriniz!")

# Programın doğrudan çalıştırıldığını kontrol eder
if __name__ == "__main__":
    ana_program()