def DecoratorFunction(orifinalFunction):
    def WrapperFunction(*args, **kwargs):
        print("Eklemek isteidğiniz kelime veya cümleler txt dosyasına eklendi")
        return orifinalFunction(*args, **kwargs)
    return WrapperFunction

@DecoratorFunction
def Ekleme (metin):
    with open("ödev 4 dosyası.txt","w",encoding=("utf-8")) as fileObjetc:
        fileObjetc.write(metin)


Ekleme("naber benim adım samet")