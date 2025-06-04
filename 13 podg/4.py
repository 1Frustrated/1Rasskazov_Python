# 1. В двумерном списке все элементы, не лежащие на главной диагонали увеличить в 2
# раза.
import random

kol_str = random.randint(2, 6)       # количество строк
el_in_kol = random.randint(1, 6)     # количество столбцов
qwe = [[random.randint(-100, 100) for el in range(el_in_kol)] for w in range(kol_str)]

ww = [[qwe[e][j] if e==j else qwe[e][j]**2 for j in range(el_in_kol)] for e in range(kol_str)]
print(ww)



# 2. Если в двумерном списке имеются положительные элементы, то вывести TRUE,
# иначе FALSE.

has_positive = any(elem > 0 for row in qwe for elem in row)

print("TRUE" if has_positive else "FALSE")