index=1
for index in range(1,10,2):
    print(f"{'*'* index:^9}")

for isim in ["samet","sude","senay"]:
    print(isim.title())

for deneme in [12,3,7,34,12,45]:
    if deneme%2==0:
        print(f"{deneme} sayısı çifttir")
    else:
        print(f"{deneme} sayısı tektir")


for ilksayı in range(1,11):
    for ikincisayi in range(1,11):
        print(f"{ilksayı*ikincisayi:4}",end='')
    print()


