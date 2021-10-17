def tcdoğrulama(tcno):
    tekSayilar=0
    ciftSayilar=0
    genelToplam=0
    sayac=1
    sayac2=1
    for sayi in tcno:
        if sayac>9:
            break
        if sayac%2==0:
            ciftSayilar+=int(sayi)
        else:
            tekSayilar+=int(sayi)
        sayac+=1
    ilkSart=(tekSayilar*7 - ciftSayilar)%10
    for sayi2 in tcno:
        if sayac2>10:
            break
        genelToplam+=int(sayi2)
        sayac2+=1
    ikinciSart=genelToplam%10


    if (ilkSart)==int(tcno[9]) and (ikinciSart)==int(tcno[10]):
        print("Tc kimlik numarası doğru ")
    else:
        print("Tc kimlik numarası yanlış")


tcdoğrulama("10129797736")






