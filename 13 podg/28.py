# 1. В двумерном списке элементы последней строки заменить на 0.
# 2. 33 работа
import random

kol_str = random.randint(2,6)
el_in_kol = random.randint(1,6)
qwe = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe)

qwe[kol_str - 1] = [0] * el_in_kol
print(qwe)
