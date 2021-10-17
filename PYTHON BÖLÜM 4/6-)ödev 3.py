çalışanListesi = [
    {"name": "Ahmet", "age": 40},
    {"name": "Ezgi", "age": 28},
    {"name": "Elif", "age": 30},
    {"name": "Mehmet", "age": 50},
]
çalışanListesi.sort(key=lambda yaş:yaş["age"])
print(çalışanListesi)
print("\n")

numbersList=[
    {"ONE":1},
    {"THREE":3},
    {"TWO":2},
    {"FİVE":5},
    {"FOUR":4}
]

print(numbersList[0])
print(list(numbersList[0])[0])
numbersList.sort(key=lambda item:item[list(item)[0]])
print(numbersList)

