with open("deneme2.txt","r") as fileObect:
    okunmuşVeri=fileObect.read()
    print(okunmuşVeri,end="")
    print(okunmuşVeri[::-1])