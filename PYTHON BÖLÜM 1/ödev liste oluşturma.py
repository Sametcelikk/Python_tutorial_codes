list=[]
list2=[]
sayac=1

while True:
    numbers=input(f"Listeye eklemek istediğiniz sayıyı girin ({sayac}): ")
    if sayac>10 and numbers=="":
        break
    elif numbers=="":
        continue
    list.append(int(numbers))
    if int(numbers) not in list2:
        list2.append(int(numbers))
    sayac+=1
print(list)
print(list2)