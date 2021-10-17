
names=[" samet", " senay" ," sude", "irem" ,"miray"]
print(names[1])
print(names[1:4])
names[0] = "süleyman"
print(names)
print(names[::2])

matrix=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix [0] [0]
print(matrix [0] [0])
for index in matrix:
    for item in index:
        print(item)


numbers=[5, 3, 11, 4, 9, 12]
numbers.append(18) #listenin sonuna yeni eleman ekleme konutu
print(numbers)
numbers.insert(0,44) #listeye istediğimiz yere yeni eleman eklememizi sağlar
print(numbers)
numbers.remove(9) #listeden istediğimiz bir elemanı silmemizi sağlar
print(numbers)
numbers.pop(2) #listeden girdiğimiz indexteki elemanı siler
print(numbers)
print(numbers.index(12)) #girdiğimiz elemanın indexini bulur
print(numbers.count(18)) #girdiğimiz elemanın listede kaç tane olduğunu sayar
numbers.sort() #listemizdeki elemanlatı büyükten küçüğe sıralar
print(numbers)
numbers.reverse() #listemizdeki elemanlatı küçükten büyüğe sıralar
print(numbers)
numbers2=numbers.copy() #listemizi başka bir listeye kopyalaamızı sağlar be yeni bir liste oluşturur
print(numbers2)
print(len(numbers)) #bir listenin içinde kaç eleman var onu gösterir

numbers.append(["samet","senay"])
print(numbers)
numbers.insert(1,1.3)
print(numbers)

