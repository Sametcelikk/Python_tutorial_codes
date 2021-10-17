from math import factorial
list1=[]
while True:
    sayı=input("Listeye eklemek istediğiniz sayıyı giriniz\n(işlemi tamamlamak iöin enter a basın): ")
    if sayı == "":
        break
    else:
        list1.append(int(sayı))


def tobyBear (*args):
    toplam=0
    if args:
        for number in args:
            if type(number) == int:
                toplam+=factorial(number)/number
    return toplam


print(f"listeniz:{list1}\nCevabınız:{tobyBear(*list1)}")
