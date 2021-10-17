def f(x):
    return 3 * x + 2


print(f(2))

f = lambda x: 3 * x + 2  # lambda isimsiz fonlardır bu fonklara isim vermemize gerek yoktur bir değişkene atarsak yeter
print(f(2))
print((lambda x: 3 * x + 2)(2))

f = lambda: "Samet"
print(f())

f = lambda x, y, z: x + 2 * y + 3 * z
print(f(2, 3, 4))
print("\n")

nameList = ["Mehmet Ali Alabora", "Ezgi mola", "Halit Ergenç", "Haluk Bilginer", "Ece Uslu", "Cüneyt arkın",
            "Ebru Cündübeyoğlu"]

nameList.sort(key=lambda name: name.split()[-1].lower())
print(nameList)
print("\n")

çalışanListesi = [
    ("Ahmet", "Satış", 10000, 0),
    ("Ezgi", "Hukuk", 8000, 0),
    ("Elif", "İdari işler", 5000, 0),
    ("Mehmet", "Yönetim", 0, 5000)
]

kur = 5.95
çalışanListesi.sort(key=lambda maaş: maaş[2] if maaş[2] != 0 else maaş[3] * kur,
                    reverse=True)  # reverse komutu en yüksekten en küçüğe sıralanmasını sağlar
print(çalışanListesi)
print("En yüksek maaş: ",max(çalışanListesi,key=lambda maaş: maaş[2] if maaş[2] != 0 else maaş[3] * kur))
print("En düşük maaş: ",min(çalışanListesi,key=lambda maaş: maaş[2] if maaş[2] != 0 else maaş[3] * kur))
print("\n")

def DenklemOluşturma (a,b,c):
    return  lambda x:a*x**2+b*x+c

print(DenklemOluşturma(2,3,-4)(1))
f=DenklemOluşturma(2,3,-4)
print(f(1))
print(f(2))
g=DenklemOluşturma(3,2,-2)
print(f(3),g(3))
print("\n")


def MyList (listeuzunluğu):
    return lambda x:[(index + x)/index for index in range(1,listeuzunluğu)]
f=MyList(10)
print(f(5))