import random
n = int(input("Введи длину списка"))

spisok = []
while len(spisok) < n:
    spisok.append(random.randint(-100,100))
if len(spisok) < 2:
    print("Нет смысла")


def check(spisok):
    f = None
    for i in range(len(spisok)):
        if f is None:
            f = spisok[i] < 0
        elif (spisok[i] > 0) == f:
            f = not f
        else:
            return i + 1
    return 0



print(spisok)
print(check(spisok))