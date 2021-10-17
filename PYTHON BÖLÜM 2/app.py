dosyaAdı=input("Açmak istediğiniz dosyanın adını giriniz: ")
satırSaysı=0
kelimeSayısı=0
enUzunKelime=0
karakterSaysı=0
with open(dosyaAdı,"r",encoding="utf-8") as metinDosyası:
    
    for lines in metinDosyası.readlines():
        satırSaysı+=1
        kelimeler=lines.split()
        kelimeSayısı+=len(kelimeler)
        for kelime in kelimeler:
            if len(kelime ) > enUzunKelime:
                enUzunKelimeKendisi=kelime





print(kelimeSayısı)
print(satırSaysı)
print(enUzunKelimeKendisi)


