print(int(True))
print(int(False))

a=60
b=bin(a)
n=50
print("a=",bin(a))  #bin komutu binary olarak yazılmasını sağlar
print(b)
print()

#OR:1 ve 1 =1  1 ve0=1  0 ve 0=0 çakışınca bu sonuçları veriyor
print(bin(a))
print(bin(n))
print(bin(a | n))
print(a | n)
print()

#AND: 1 ve 1=1  1 ve 0=0  0 ve 0=0 çakışınca bu sonuçları veriyor
print(bin(a))
print(bin(n))
print(bin(a & n))
print(a & n)
print()

#XOR: 1 ve 1=0  1 ve 0=1  0 ve 0=0 çakışınca bu sonuçları veriyor
print(bin(a))
print(bin(n))
print(bin(a ^ n))
print(a ^ n)
print()

#Complement-DEĞİL: 0 ları 1 e 1 leri sıfıra çevirir
print(bin(a))
print(bin(n))
print(bin(~a))
print(bin(~n))
print()

#SHIFT RIGHT - Sağa kaydırma
print(bin(a))
print(bin(a >> 1))
print()

#SHIFT LEFT - Sola kaydırma
print(bin(a))
print(bin(a<<1))

