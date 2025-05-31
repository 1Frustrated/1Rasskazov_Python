# 1. В двумерном списке найти сумму элементов первых двух строк.
import random

kol_str = random.randint(2,6)
el_in_kol = random.randint(1,6)
qwe = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe)

while True:
    try:
        ww = sum([w for w in qwe[0]])
        ww2 = sum([w for w in qwe[1]])

        print(ww + ww2)
        break
    except IndexError:
        print("LL")



# 2. В двумерном списке найти минимальный и максимальные элементы.

ww3 = min([el for w in qwe for el in w])
print(ww3)
ww3 = max([el for w in qwe for el in w])
print(ww3)