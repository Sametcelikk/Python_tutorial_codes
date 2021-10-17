dosyaAdı=input("Taramak İstediğiniz Dosyanın adını girin: ")
satırSayısı=0
kelimeSayısı=0
enUzunKelime=0
karakterSayısı=0
enUzunKelimeİsmi=""
with open(dosyaAdı,encoding="utf-8") as fileObject:
    for satır in fileObject:
        satırSayısı+=1
        kelimeler=satır.split()
        kelimeSayısı+=len(kelimeler)
        karakterSayısı+=len(list(satır))
        for kelime in kelimeler:
            if len(kelime) > enUzunKelime:
                enUzunKelime = len(kelime)
                enUzunKelimeİsmi = kelime

print(f"Metnin satır sayısı: {satırSayısı}")
print(f"Metindeki kelime saysı: {kelimeSayısı}")
print(f"Metindeki en uzun kelime: {enUzunKelimeİsmi} ve karakter sayısı: {enUzunKelime} ")
print(f"Metnin karakter sayısı: {karakterSayısı}")


