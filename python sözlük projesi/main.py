sözlük={
    "this":("zamir","Bu , Şu"),
    "is":("fiil","Olmak"),
    "a":("belirteç","Bir"),
    "book":("isim","Kitap"),
    "pen":("isim","Kalem"),
    "car":("isim","araba"),
    "house":("isim","ev"),
    "homework":("isim","Ev Ödevi")
}
while True:
    çevirilmişCümle = ""
    cümle = input("Bir cümle girin (ÇIKMAK İÇİN ENTER A BASIN): ")
    print()
    if cümle == "":
        break

    for noktalama in ".!?,=_-":
        cümle=cümle.replace(noktalama,"")

    kelimeler = set(cümle.lower().split())

    enUzunKelime=1
    for kelime in kelimeler:
        if enUzunKelime < len(kelime):
            enUzunKelime=len(kelime)


    for kelime in kelimeler:
        kelimeTanımı=sözlük.get(kelime)
        if kelime not in sözlük:
            print(f"{kelime:<{enUzunKelime}} : Bu kelime bulunamadı")
        else:
            print(f'{kelime.upper():<{enUzunKelime}} = ({kelimeTanımı[0].title():^8}) {kelimeTanımı[1].title()}')
    print()
print("Kullanıcı çıkışı")



