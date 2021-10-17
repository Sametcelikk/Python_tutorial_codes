import random
sayac=1
hak=3
sayı=random.randint(1,5)


while sayac<=3:
    tahmin = int(input(f"Bir ve beş arasında bir sayı tahmin edin {hak} hakknız kaldı"))
    hak-=1
    if tahmin==sayı:
        print("Tahmin doğru Tebrikler")
        break
    elif hak==0:
        print("Tahmin hakkınız kalmadı ")
        sayac += 1
    else:
        print(f"Tahmin yanlış")

        sayac+=1
print("Oyun bitti :)")