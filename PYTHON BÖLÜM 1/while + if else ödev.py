
index=1
while index<2:
    ısım = input("İsminizi girini: ")
    if len(ısım)<3 or len(ısım)>15:
        print("Hatalı giriş yaptınız tekrar deneyin")
    else:
        print(f"Merhaba {ısım.title()}")
        break

