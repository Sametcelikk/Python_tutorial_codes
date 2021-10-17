def lisiteolusturma():
    liste1=[]
    while True:
        item=input("bir eleman giriniz: ")
        if item == "":
            break
        liste1.append(int(item))
    print(liste1)


lisiteolusturma()