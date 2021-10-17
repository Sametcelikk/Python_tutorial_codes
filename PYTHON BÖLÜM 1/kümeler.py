numbers=[1,1,2,3,4,5,6,6,7]
kume=set(numbers) #set küme yapma fonksiyonudur. Kümelerde tekrar eden elemanlar olmaz
print(kume)

kume2={2,3,5,7,11,13} #kümeyi süslü parantezle tanımlayabiliriz
kume2.add(17) #kümeye eleman eklemek için add komutu kullanılır
print(kume2)
kume2.remove(11) #kümeden bir eleman silmemizi sağlar
print(kume2)
kume2.update({23,29},[31,37],(44,70)) #kümeye bir veya birden fazla eleman eklememizi sağlar
print(kume2)
kume2.clear() #tüm kümeyi temizlemeni sağlar ama kümeyi silmez
print(kume2)

evenNumbers={number for number in  range(2,51,2)}
print(evenNumbers)
oddNumbers={number for number in range(1,51,2)}
print(oddNumbers)
üçünKatları={number for number in range(3,51,3)}
print(üçünKatları)
beşinKatları={number for number in range(5,51,5)}
print(beşinKatları)
print(len(evenNumbers))
print(len(oddNumbers))
print(len(üçünKatları))
print(len(beşinKatları))

print(evenNumbers | oddNumbers) # | işareti iki kümenin birleşimini oluşturur
print(evenNumbers.union(oddNumbers)) #union komutu da iki kümenin birleşmesini sağlar
print(evenNumbers & beşinKatları) # & işareti iki  kümenin kesişimini bulur
print(evenNumbers.intersection(beşinKatları)) #intersection kommutu da iki kümenin kesişimini verir
print(evenNumbers - beşinKatları) # - işareti iki kümenin farkını verir
print(evenNumbers.difference(beşinKatları)) # difference komutu da iki kümenin farkını verir
print(evenNumbers ^ üçünKatları) #iki kümenin kesişen eleanlarını silip kümeleri birleştirir
print(evenNumbers.symmetric_difference(üçünKatları)) #bu komut da iki kümenin kesişen eleanlarını silip kümeleri birleştirir

ornekKume={3,5,7}
if ornekKume.issubset(oddNumbers): #issubset komutu bir kümenin başka bir kümenin alt kümesi olup olmadığını kontrol eder
    print("ornek küme tek sayılar kümesinin alt kümesidir")
if oddNumbers.issuperset(ornekKume): #isduperset komutu bir kümenin başka bir kümenin kapsayanı olup olmadığını kontrol eder
    print("tek sayılar ornek kümenin kapsayanıdır")

#BİR STRİNGİ KÜMEYE ÇEVİRME#

string="Samet eve gel"
stringSet=set(string)
print(stringSet)
stringSet2=set(string.split()) # stringdeki kelimeleri algılayıp kelimeyi harflere ayırmadan bi bütün olarak elemana çevirir
print(stringSet2)

sesliHarfler={"a","e","ı","i","o","ö","ü","u"}
kesişim=sesliHarfler & stringSet
print(kesişim)
print(len(kesişim))
