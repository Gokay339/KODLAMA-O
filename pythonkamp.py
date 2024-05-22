ogrenciler = ["Gökay Adıgüzel","Emirhan Özkan","Berkay Şahin"]

def ogrenciekle(isimsoyisim):
    ogrenciler.append(isimsoyisim)
    print(f"{isimsoyisim} Öğrencimiz Başarıyla Sisteme Eklendi")
    
def ogrencisil(isimsoyisim):
    if isimsoyisim in ogrenciler:
        ogrenciler.remove(isimsoyisim)
        print(f"{isimsoyisim} Öğrencimiz Başarıyla Sistemden Silindi")
    else:
        print(f"{isimsoyisim} İsimli Öğrenci Listede Bulunamadı.")
        
def ogrencilistele():
    print("Tüm Öğrenciler : ")
    for i, ogrenci in enumerate(ogrenciler, start=1):
        print(f"{i}. {ogrenci}")

def ogrenciekletoplu(isimsoyisim):
    ogrenciler.append(isimsoyisim)
    print(f"{isimsoyisim} Öğrencimiz Başarıyla Sisteme Eklendi")

def ogrencisiltoplu(isimsoyisim):
    if isimsoyisim in ogrenciler:
        ogrenciler.remove(isimsoyisim)
        print(f"{isimsoyisim} Öğrencimiz Başarıyla Sistemden Silindi")
    else:
        print(f"{isimsoyisim} İsimli Öğrenci Listede Bulunamadı.")

def ogrenci_numarasi_bul(isimsoyisim):
    if isimsoyisim in ogrenciler:
        numara = ogrenciler.index(isimsoyisim) + 1
        print(f"{isimsoyisim} Öğrencisinin Numarası: {numara}")
    else:
        print(f"{isimsoyisim} İsimli Öğrenci Listede Bulunamadı.")

print("Eğitim Kampımıza Hoşgeldiniz .!\n\n1)Öğrenci Ekle\n2)Toplu Öğrenci Ekle\n3)Öğrenci Sil\n4)Toplu Öğrenci Sil\n5)Öğrencileri Listele\n6)Öğrenci Numarasını Bul\n7)Çıkış\n")
def islemler():
    secenekler = int(input("Lütfen Yapmak İstediğiniz İşlemi Tuşlayın : "))

    if secenekler == 1:
        print("Öğrenci Ekleme Sistemine Hoşgeldiniz")
        ekle = input("Lütfen Eklemek İstediğiniz Öğrencinin Adını Ve Soyadını Girin : ")
        ogrenciekle(ekle)
        islemler()
        
    elif secenekler == 2:
        print("Toplu Öğrenci Ekleme Sistemine Hoşgeldiniz")
        sayı = int(input("Lütfen Eklemek İstediğiniz Öğrenci Sayısını Girin: "))
        for tekle in range(sayı):
            tekle = input("Lütfen Eklemek İstediğiniz Öğrencinin İsmini Ve Soyismini Giriniz : ")
            ogrenciekletoplu(tekle)
        islemler()
    
    elif secenekler == 3:
        print("Öğrenci Silme Sistemine Hoşgeldiniz")
        sil = input("Lütfen Silmek İstediğiniz Öğrencinin Adını Ve Soyadını Girin :")
        ogrencisil(sil)
        islemler()
    
    elif secenekler == 4:
        print("Toplu Öğrenci Silme Sistemine Hoşgeldiniz")
        sayı = int(input("Lütfen Silmek İstediğiniz Öğrenci Sayısını Girin :"))
        for tsil in range(sayı):
            tsil = input("Lütfen Silmek İstediğiniz Öğrencinin İsmini Ve Soyismini Giriniz : ")
            ogrencisiltoplu(tsil)
        islemler()
        
    elif secenekler == 5:
        print("Öğrenci Listeleme Sistemine Hoşgeldiniz")
        ogrencilistele()
        islemler()
    
    elif secenekler == 6:
        print("Öğrenci Numarasını Bulma Sistemine Hoşgeldiniz")
        isim_soyisim = input("Lütfen Öğrencinin İsmini ve Soyismini Girin : ")
        ogrenci_numarasi_bul(isim_soyisim)
        islemler()
        
    elif secenekler == 7:
        print("\nÇıkış Yapılıyor...")
        exit()                                                    #DÖNGÜDE OLMADIĞIMIZ İÇİN BREAK KULLANAMAYIZ
    
    else:
        print("Lütfen Geçerli Bir Sayı Tuşlayınız ")
islemler()

islemler()
