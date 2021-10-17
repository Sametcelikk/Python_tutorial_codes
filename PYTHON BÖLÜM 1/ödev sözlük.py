yasaklıKelimeler={"aq":"**","amk":"***","siktir":"******"}
sonCümle=""

cümle=input("Bir cümle giriniz: ")

for kelime in cümle.split():
    if kelime in yasaklıKelimeler:
        sonCümle+=f"{yasaklıKelimeler.get(kelime)} "
    else:
        sonCümle+=f"{kelime} "

print(sonCümle)

