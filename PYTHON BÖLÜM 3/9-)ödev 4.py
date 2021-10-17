import base64

with open("deneme.txt","rb") as fileObject:
    okunmuşVeri=fileObject.read()
okunmuşVeriBase64=base64.b64encode(okunmuşVeri)

with open("deneme2.txt","wb") as fileObject:
    fileObject.write(okunmuşVeriBase64)











# with open("deneme.txt","r",encoding="utf-8") as fileObject:
#     okunmuşVeri=fileObject.read()
# okunmuşVeriBinary=okunmuşVeri.encode("utf-8")
# okunmuşVeriBase64=base64.b64encode(okunmuşVeriBinary)
# string=okunmuşVeriBase64.decode("utf-8")
# with open("deneme2.txt","w",encoding="utf-8") as fileObject:
#     fileObject.write(string)