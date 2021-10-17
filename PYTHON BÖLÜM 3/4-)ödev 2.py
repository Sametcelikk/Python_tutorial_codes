list1=list()
list2=list()
while True:
    item=input("Lütfen sayı giriniz: ")
    if item == "":
        break
    list1.append(int(item))
    print(f"liste: {list1}. Ekleme yapmak istemiyorsanız enter a basın")
list1.sort()

for item in list1:
    tuple=(item,item*item)
    list2.append(tuple)
print(f"Son liste:{list2}")



