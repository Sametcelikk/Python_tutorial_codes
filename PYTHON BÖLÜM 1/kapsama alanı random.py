import random

sifre=""
karakterler="ashdgqydıuqwu81623812oıkb654"
for index in range(random.randint(8, 15)): #karakter havuzundan rastgele karakterleri seçip rastgele uzunlukta şifre oluşturuyor
    sifre+=random.choice(karakterler)

print(sifre)
def artikyil():
        if yil%4==0:
            if yil%100==0:
                if yil%400==0:
                    return True
                return False
            else:
                return True
        return False


for yil in range(2020 , 1900 ,-1):
    if artikyil():
        print(f"{yil} yılı artık yıldır")






artikyil()


