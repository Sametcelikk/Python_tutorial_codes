import math
a=int(input("a sayısını giriniz: "))
b=int(input("b sayısını giriniz: "))
c=int(input("c sayısını giriniz: "))
delta=b**2-4*a*c
if delta>0:
    print(f"birinci kök: {(-b+math.sqrt(delta))/2}\nikinci kök: {(-b-math.sqrt(delta))/2} ")
elif delta==0:
    print(f"İki kök vardır ve bu kökler çakışıktır. Kökler:{-b/2*a}'dir")
else:
    print("Reel kök yoktur")