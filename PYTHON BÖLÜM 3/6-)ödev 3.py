while True:
    komut=input("İşlemi giriniz (sayı işlem sayı): ")
    elemanlar=komut.split()

    if len(elemanlar) !=3:
        print("Yanlış işlem girdiniz")
        exit(0)
    try:
        sayı1=int(elemanlar[0])
        işlem=elemanlar[1]
        sayı2=int(elemanlar[2])
    except ValueError:
        print("Yanlış işlem yaptınız lütfen sayı işlem sayı şeklinde yazıp işleminizi yapın")
    else:
        break

if işlem =="+":
    print(f"Sonuç:{sayı1+sayı2}")
elif işlem =="-":
    print(f"Sonuç:{sayı1-sayı2}")
elif işlem =="*":
    print(f"Sonuç:{sayı1*sayı2}")
elif işlem =="/":
    print(f"Sonuç:{sayı1/sayı2}")

