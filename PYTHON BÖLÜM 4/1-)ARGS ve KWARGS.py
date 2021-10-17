def semple(*numbers):  # * komutu ile fonksiyona ne kadar değişken tanımlayacağımı baştan belirlemek zorunda kalmadım
    sonuç = 1
    for sayı in numbers:
        if type(sayı) == int or type(sayı) == float:
            sonuç *= sayı
    return sonuç


myList = [5, 6, 7, 8, "samet", 12.5]
print(semple(*myList),"asd")  # listenin başına * koymazsak listeyi tek bir eleman olarak görüp içindekileri okumayacak
print(semple(1, 2, 3, 4, 5, "samet", 2.5))
print(*myList)
print()

myFruits = {"Ananas": 52, "Kivi": 49, "Nar": 63, "Greyfurt": 41, "Elma": 58, "Karpuz": 26}


def ProperCalorie(**meyveler):  # ** isareti key value ikilisi yani sözlük atamamızı sağlar
    for meyveİsmi,meyveKalorisi in meyveler.items():
        if meyveKalorisi < 50:
            print(f"{meyveİsmi}: {meyveKalorisi} kaloridir")


ProperCalorie(**myFruits)
print(semple(myList))