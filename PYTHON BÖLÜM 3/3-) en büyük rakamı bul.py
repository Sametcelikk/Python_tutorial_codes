import math

def maxRakamıBul(sayı):
    kalan=sayı
    basamakSayısı=math.floor(math.log10(sayı))  #sayımın basamağının bir eksiğini bulacak
    maxRakam=0

    while kalan>0:
        soldakiRakam=math.floor(kalan / pow(10,basamakSayısı))
        if soldakiRakam > maxRakam:
            maxRakam=soldakiRakam
        kalan = kalan - soldakiRakam * pow(10,basamakSayısı)
        basamakSayısı-=1
    return maxRakam


sayı=int(input("Lütfen bir sayı giriniz: "))
print(f"{sayı} sayısının en büyük rakamı {maxRakamıBul(sayı)}")
