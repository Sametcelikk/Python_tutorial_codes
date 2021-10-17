list1=list()
while True:
    try:
        number=int(input("Listeye eklemek istediğiniz sayıyı giriniz "))
        if str(number) == "":
            break
    except ValueError:
        print("Lütfen sayı giriniz")
    else:
        list1.append(number)
print(list1)
print(list1[::-1])
