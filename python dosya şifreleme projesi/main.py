import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend


def keyÜretici(şifreParam):
    if type(şifreParam) == str:
        şifreParam=şifreParam.encode("utf-8")
    keyDerivationFunction=Scrypt(
        salt=b'ABCDEFGHIJKLMNOP',
        length=32,
        n=2**14,
        r=8,
        p=1,
        backend=default_backend()
    )
    deriveKey=keyDerivationFunction.derive(şifreParam)
    key=base64.urlsafe_b64encode(deriveKey)
    return key



def şifreleme(metinParam,şifreParam):
    convertChunkToString=False
    if type(metinParam) == str:
        metinParam=metinParam.encode("utf-8")
        convertChunkToString=True
    key=keyÜretici(şifreParam)
    fernet=Fernet(key)
    şifrelenmişMetin=fernet.encrypt(metinParam)
    if convertChunkToString == True:
        şifrelenmişMetin=şifrelenmişMetin.decode("utf-8")
    return şifrelenmişMetin


def şifreÇözme (metinParam,şifreParam):
    key=keyÜretici(şifreParam)
    fernet=Fernet(key)
    try:
        çözülmüşMetin=fernet.decrypt(metinParam)
    except Exception:
        return None
    return çözülmüşMetin



def dosyaŞifreleme (fileNameParam,şifreParam):
    with open(fileNameParam,"rb") as fileObject:
        okunmuşDosya=fileObject.read()
    şifrelenmişDosya=şifreleme(okunmuşDosya,şifreParam)
    with open(f"{fileNameParam}.enc","wb") as fileObject:
        fileObject.write(şifrelenmişDosya)
        print(f"şifrelenmiş dosya '{fileNameParam}.enc' adıyla oluşturuldu")


def dosyaÇözme(fileNameParam,şifreParam):
    with open(f"{fileNameParam}","rb") as fileObject:
        okunmuşDosya=fileObject.read()
    çözülmüşDosya=şifreÇözme(okunmuşDosya,şifreParam)
    if çözülmüşDosya == None:
        print("Hatalı şifre")
    else:
        with open(f"{fileNameParam}.dec","wb") as fileObject:
            fileObject.write(çözülmüşDosya)
            print(f"Şifresi çözülmüş dosya '{fileNameParam}.dec' adıyla oluşturuldu")


while True:
    komut=input("Lütfen yapmak istediiniz işlemi giriniz\nŞifreleme için 'S' Şifre çözmek için 'C': ").upper()
    if komut == "S" or komut=="C":
        break
    else:
        print("!!! İşlem türünü S veya C olarak giriniz !!!")
şifre=(input("Şifre giriniz: "))
fileName=input("İşlem yapmak istediğiniz dosya adını giriniz: ")

if komut == "S":
    dosyaŞifreleme(fileName,şifre)
elif komut == "C":
    dosyaÇözme(fileName,şifre)






