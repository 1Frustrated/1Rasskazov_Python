# 1. В двумерном списке найти минимальный элемент в предпоследней строке.


import random

kol_str = random.randint(2,6)
el_in_kol = random.randint(1,6)
qwe = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe)
while True:
    try:
        minim = min(row for row in qwe[-2])
        print(minim)
        break
    except IndexError:
        print("предпоследней строки нет")


# 2. В двумерном списке элементы на главной диагонали увеличить в 2 раза.

qwe2 = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]

qwe2_doubled_diag = [[qwe2[i][j] * 2 if i == j else qwe2[i][j] for j in range(el_in_kol)]for i in range(kol_str)]
print(qwe2_doubled_diag)