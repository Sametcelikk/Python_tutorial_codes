customer={
    "name":"samet",
    "email":"samet@gmail.com",
    "phoneNumber":"5432362697"
}

print(customer)

customer2=dict(name="senay",email="senay@gmail.com",phone="5136548924")
print(customer2)
print()


print(customer["email"]) #sözlükteki anahtarın değerini bulmamızı sağlar
customer["name"] = "irem" #anahtarın değerini değiştirmemizi sağladı
print(customer["name"])

customer["customerId"] = "123" #sözlüğümüzde olmayan bir anahtara değer atamaya çalışırsak o anahtar oluşturulur ve değer atanır
print(customer)

print(customer.get("date","01.01.2000")) #get metodu girdiğimiz anahtar yoksa belirlediğimiz varsayılan mesajını yazdırı
print(customer.get("name"))
print()

for key in customer:
    print(key)

for key in customer.keys():
    print(f"{key} = {customer[key]}")

customerItemsList=list(customer.items())
print(customerItemsList,"aaaaaaaaaaaaaaaaaaaaaa")
for key,value in customerItemsList:
    print(f"{key} = {value}")

customer.pop("phoneNumber") #sözlükten bir anahtarı ve onun değerini silmemizi sağlar
print(customer)

customer.clear() #sözlüğü ortadan kaldırmaz ama içini boşaltır
print(customer)
customer.update(name="sude",email="sude@gmail.com") #listeye yeni anahtar ve değerini eklememizi sağlar
print(customer)
print("\n......................................\n")

#MİNİ ÖDEV#
sozluk1={"1":"bir", "0":"sıfır", "2":"iki", "3":"üç", "4":"dört"}
outputString=""
number=input("Bir sayı girin: ")

for digit in number():
    outputString += f"{sozluk1.get(digit,'*')} "

print(outputString)




