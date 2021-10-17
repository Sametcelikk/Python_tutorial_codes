import pickle
import  os   #dosaynın olup olmadığını öğrenmemizi sağlayan modül


def anaMenü():
    print("1. Kayıtları Listele")
    print("2. Kayıt Ara")
    print("3. Kayıt Ekle")
    print("4. Kayıt Sil")
    print("5. çıkış")
    print()


def menüSeçeneği():
    while True:
        anaMenü()
        seçim=input("Seçenek (1-5): ")
        if seçim.isdigit() and 1<= int(seçim) <=5:
            break
        print("Lütfen 1 ile 5 arasında bir sayı giriniz")
    return seçim



def işlemKısmı():
    while True:
        seçim=menüSeçeneği()
        if seçim == "1":
            kayıtlarıListele()
        elif seçim == "2":
            kayıtAra()
        elif seçim == "3":
            kayıtEkle()
        elif seçim == "4":
            kayıtSil()
        elif seçim == "5":
            break



def kayıtlarıListele():
    okunmuşDosya=dosyaOkuma()
    print(f"Kayıt Saysı: {len(okunmuşDosya)}\n")
    print(f"{'İSİM':^10} {'SOYİSİM':^10} {'NUMARA':^11}" )
    for kayıt in okunmuşDosya:
        print(f"{kayıt.get('isim',''):10.10} {kayıt.get('soyisim',''):10.10} {kayıt.get('numara',''):10.10}")



def kayıtAra():
    okunmuşDosya=dosyaOkuma()
    print("Kayıt arama\n")
    isim = input("İsim: ")
    soyisim = input("Soyisim: ")
    kayıtListesi=lıstedenKayıtBulma(isim,soyisim)
    print("Telefon Numarası:",end="")
    for kayıt in kayıtListesi:
        print(f"{kayıt.get('numara'):11.11}",end="")
    print("\n")



def kayıtEkle():
    print("Yeni Kayıt Oluşturma")
    isim=input("İsim: ")
    soyisim=input("Soyisim: ")
    numara=input("Telefon numarası: ")
    print(f"Yeni kayıt: {isim} {soyisim} - {numara}")
    if eminMisin():
        dosyayaKayıtEkle(isim,soyisim,numara)
    print("Kayıt başarıyla eklendi\n")


def kayıtSil():
    print("Kayıt Sil")
    isim = input("İsim: ")
    soyisim = input("Soyisim: ")
    kayıtListesi=lıstedenKayıtBulma(isim,soyisim)
    print("Telefon Numarası:", end="")
    for kayıt in kayıtListesi:
        print(f"{kayıt.get('numara'):11.11}", end="")
        print("\n")
    if eminMisin():
        dosyadanSilme(kayıtListesi)
        print("Kayıt Silindi\n")


def dosyadanSilme(kayıtListesiParam):
    kayıtListesi=dosyaOkuma()
    for kayıt in kayıtListesi:
        for silinecekKayıt in kayıtListesiParam:
            if kayıt.get("isim") == silinecekKayıt.get("isim") and kayıt.get("soyisim") == silinecekKayıt.get("soyisim"):
                kayıtListesi.remove(silinecekKayıt)
    dosyayaYazma(kayıtListesi)


def lıstedenKayıtBulma(isimParam,soyisismParam):
    kayıtListesi=dosyaOkuma()
    cevapListem=list()
    for kayıt in kayıtListesi:
        if kayıt.get("isim").upper() == isimParam.upper() and kayıt.get("soyisim").upper() == soyisismParam.upper():
            cevapListem.append(kayıt)
    return cevapListem


def dosyayaKayıtEkle(isimParam, soyisimParam, numaraParam):
    kayıtListesi= dosyaOkuma()
    kayıtSözlüğü=dict(isim=isimParam,soyisim=soyisimParam,numara=numaraParam)
    kayıtListesi.append(kayıtSözlüğü)
    dosyayaYazma(kayıtListesi)


def dosyaOkuma():
    if os.path.isfile("kayıtlar.bin"):    #kayıtlar.bin dosyası varsa demek
        with open("kayıtlar.bin","rb") as fileObject:
            kayıtListesi=pickle.load(fileObject)
    else:
        kayıtListesi=list()
    return kayıtListesi


def dosyayaYazma(kayıtListesiParam):
    with open("kayıtlar.bin","wb") as fileObject:
        pickle.dump(kayıtListesiParam,fileObject)


def eminMisin():
    while True:
        cevap=input("Emin isiniz (E/H): ")
        print()
        if cevap.lower() == "e":
            return True
        elif cevap.lower() == "h":
            return False


işlemKısmı()
