sayaç=0
while True:
    sayaç+=1
    try:
        age = int(input("yaşınızı giriniz: ")) #try except arasına yazılan kodda belirlediğimiz bir hataya rastlanırsa
                                               #except komutunda verdiğimizz görevi yapmasını sağlarız
    except ValueError:
        print("yanlış değer girdiniz. Sayı değeri giriniz.")
    except Exception as exceptionObject:
        print("Beklenmedik bir hata oluştu:",exceptionObject) #exception komutu bilmediğimiz herhangi bir hata oluşursa onun yerine
                                                             #istediğimiz komutu yapmasını sağlar
    else:   #except komutu çalışmazsa else komutu çalışır
        print(age)
        break
    finally:  #bu komut ne olursa olsun çalışır
        print(f"Döngü {sayaç} kere çalıştı")
        if sayaç > 5:
            print("Çok fazla deneme yapıldı 1 saat sonra deneyiniz.")
            break
