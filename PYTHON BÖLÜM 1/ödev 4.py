ad=input("İsminizi girin: ")
soyad=input("Soyadınızı girin: ")

if len(ad)<3 or len(ad)>15:
    print("Karakter sayısı uyuşmuyor")
elif len(soyad)<3 or len(soyad)>15:
    print("Karakter sayısı uyuşmuyor")

else:
    print(f"Merhaba {ad.title()} {soyad.upper()} ")