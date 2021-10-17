list1=[]
sayac=1
while True:
    name = input("İsim Giriniz: ")
    if sayac > 5 and name == "":
        break
    if name=="":
        print("Geçersiz karakter")
        continue
    if name in list1:
        print("Bu ismi daha önceden girdiniz başka bir isim giriniz:")
        continue

    else:
        list1.append(name)

    sayac += 1


print(f"İsim listesi: {list1}")
