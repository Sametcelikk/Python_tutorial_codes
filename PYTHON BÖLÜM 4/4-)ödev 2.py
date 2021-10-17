def Fibonacci(elemanSayısı):
    resultList = list()
    if elemanSayısı <= 0:
        return resultList
    resultList.append(0)
    if elemanSayısı == 1:
        return resultList
    resultList.append(1)
    if elemanSayısı == 2:
        return resultList
    for index in range(2, elemanSayısı + 1):
        resultList.append(resultList[-2] + resultList[-1])
    return resultList


print(Fibonacci(15))
print(sum(Fibonacci(15))) #sum komutu liste içindeki tüm elemanları toplamamızı sağllar
