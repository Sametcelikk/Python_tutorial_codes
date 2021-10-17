import base64
from math import log,ceil

string="Merhaba benim adim samet"
stringAsBytes=string.encode("utf-8")

stringAsBase64=base64.b64encode(stringAsBytes)
print(stringAsBase64)

string=stringAsBase64.decode("utf-8")
print(string)

newString=base64.b64decode(stringAsBase64)
newString2=newString.decode("utf-8")
print(newString2)
print("\n\n")

number=23123123123123
print(f"{number}sayımız bit olarak: {bin(number)}")

numberOfBytes=ceil(ceil(log(number,2))/8)

numberAsBytes=number.to_bytes(numberOfBytes,byteorder="little")
numberAsBase64=base64.b64encode(numberAsBytes)
print(f"Base64 olarak: {numberAsBase64}")

newNumbers=base64.b64decode(numberAsBase64)
newNumbers2=int.from_bytes(newNumbers,byteorder="little")
print(newNumbers2)
