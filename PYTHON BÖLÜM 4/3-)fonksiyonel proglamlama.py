def Calculate(func, x, y):
    return func(x, y)


def Add(x, y):
    return x + y


def Subtract(x, y):
    return x - y


print(Calculate(Add, 2, 3))
print(Calculate(Subtract, 2, 3))

words = dictionary = ["fox", "boss", "orange", "cup", "fury", "toes"]
word = words[0]
print(word[0:-1:])


def Puralize(words):
    results = list()
    for index in range(len(words)):
        word = words[index]
        if word.endswith("s") or word.endswith("x"):
            word += "es"
        elif word.endswith("y"):
            word = word[:-1] + "ies"
        else:
            word += "s"
        results.append(word)
    return results


print(Puralize(dictionary))
print(dictionary)
print()


def Helloworld(param):
    def World(world):
        print(param, world)

    return World


f = Helloworld("hello")
f("world")


def ActionOne(param):
    print(param)


def ActionTwo(param):
    print(param)


myFunctionList=[ActionOne,ActionTwo]
myFunctionList[0]("Deneme")


def SenpleFunc(number,callback1,callback2):
    if number % 2 ==0:
        return callback1
    return callback2


def Callback1(number):
    print("1",number)
def Callback2(number):
    print("2",number)

number=20
f=SenpleFunc(number,Callback1,Callback2)
f(number)