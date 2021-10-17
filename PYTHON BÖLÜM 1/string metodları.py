ornek="Bugün Hava Güneşli Yarın yağmurlu olacak"
print(ornek)
print(len(ornek)) #karakter saysı
print(ornek.upper()) #tüm karakterleri büyük harfle yazar
print(ornek.lower()) #tüm karakterleri küçük harfle yazar
print(ornek.title()) #kelimelerin ilk harflerini büyük yapar
print(ornek.find("a")) #karakterin bulunduğu ilk indeksi bize verir
print(ornek.replace("Yarın","perşembe")) #bir stringteki harf ya da kelimeleri başka kelimeye veya harfle değiştirir
print("Hava"in ornek) #stringin içinde istediğimiz ifade varsa true yoksa false
print(ornek.count("a")) #istediğimiz harf ya da kelimenin stringde kaç tane olduğunu hesaplar
print(".\n.\n.\n.\n.\n.\n.")

x=4.75
y=-3.9
print(round(x)) #sayıyı yuvarlar
print(abs(y)) #sayının pozitif değerini yazar