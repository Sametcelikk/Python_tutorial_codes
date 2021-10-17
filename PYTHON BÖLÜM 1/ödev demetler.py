items=[(11,22),(33,55),(55,11),(11,44)]
list1=[]
for index1 in items:
    for index2 in index1:
        if 11 == index2:
            list1.append(index1)

print(list1)