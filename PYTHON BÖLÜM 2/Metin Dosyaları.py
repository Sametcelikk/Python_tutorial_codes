with open("deneme.txt","w",encoding="utf=8") as metinDosyası: #metin dosyasını açıp bir değişkene atamamızı sağlar
    kelimeler=["bu\n","bir\n","deneme\n","metnidir\n"]
    metinDosyası.writelines(kelimeler) #bu komut listedeki kelieleri metin dosyamıca eklememizi sağlar
    metinDosyası.write("dikkatli olun") #bu komut da elle ekleme yapmamızı sağlar

with open("deneme.txt","r",encoding="utf-8") as metinDosyası2: #"r" yazdığımız için bu sefer belirlediğimiz dosyayı okudu
    okunmuşVeri=metinDosyası2.read() # read konutu okunmuş dosyayı terminale yazdırmamızı sağladı
    print(okunmuşVeri)
    print("\n..................\n")
with open("deneme.txt", "r", encoding="utf=8") as metinDosyası2:
    for satırlar in metinDosyası2.readlines():
        print(satırlar,end="")
print("\n")
with open("deneme.txt", "r+", encoding="utf=8") as metinDosyası2: #var olan dosyayı hem okumamızı hem de ona ekleme yapmamızı sağlar ama dosya yoksa hata verir
    for satırlar in metinDosyası2.readlines():
        print(satırlar,end="")
    metinDosyası2.write(".")

#Bu w r r+ ve w+ komutlerını kullanmaktansa a komutunu kullanarak hem dosya okuyabilir hem onu oluşturabilir hem de ekleme yapacak isek oluşturmakla uğraşmayız
#a komutu r+ komutunun aksine dosyamızı oluşturup ona ekleme yapar a kommutunu metin dosyaları 2 dosyasında yazdım oraya bak
#ve her zaman a modunda açmayız ihtiyacımıza göre tercih ederiz

