kelime=input("Polindrom olup olmadığını kontrol etmek için bi kelime giriniz: ")
kelime2=kelime[::-1]
if kelime2 == kelime:
    print("Bu kelime polindromdur")
else:
    print("Bu kelimde polindrom değildir")
print(f"kelime 1 = {kelime}")
print(f"kelime 2 = {kelime2}")