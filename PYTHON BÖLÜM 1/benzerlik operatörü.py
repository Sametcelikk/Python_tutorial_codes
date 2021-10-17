string1="samet"
string2="samet"

print(id(string1))
if id(string1== id(string2)):
    print("aynı karakterler")

if string1 is string2:
    print("aynı karakterler")

deger1=1
deger2=2

print(f"değer1 = {deger1} değer2 = {deger2}")
if type(deger1) is type(deger2):
    deger1 , deger2 = deger2 , deger1
    print(f"değer1 = {deger1} değer2 = {deger2}\nDeğerler değiştirildi")
else:
    print("Değişkenler aynı değil değerler değiştirilemiyor")
