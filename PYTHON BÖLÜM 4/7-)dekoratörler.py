def DecoratorFunction(originalFunction):
    def WrapperFunction(*args, **kwargs):
        print("Wrapper işleri")
        print(f"Orijinal fonksiyon '{originalFunction.__name__}' öncesi")

        def CanNotRun():
            print(f"Bu fonksiyon izinli değil: {originalFunction.__name__}")

        if canRun == False:
            return CanNotRun()

        return originalFunction(*args, **kwargs)

    return WrapperFunction


@DecoratorFunction  # Bu ibare fonksiyonumuzu alıp dekoratör fonksiyonun parametresine ekliyor bir daha bizi elle eklememize gerek kalmıyor
def MyFunction():
    print("Bazı işler yapıyorum")


@DecoratorFunction
def DisplayInfo(name, age):
    print(f"Benim adım {name} ve yaşım {age}")

canRun=False
MyFunction()  # burda fonksiyonumuz yukarıda yaptğımız işlemden dolayı dekoratör fonksiyonla birlikte çalışıyor
canRun=True
DisplayInfo("samet", 21)
