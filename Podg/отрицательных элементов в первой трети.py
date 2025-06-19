# В двумерном списке найти сумму отрицательных элементов в первой трети
# # матрицы

import random
kol_str = 6       # количество строк
el_in_kol = 4     # количество столбцов
qwe = [[random.randint(-100, 100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe)

first_third_rows = kol_str // 3
if first_third_rows == 0 and kol_str > 0:
    first_third_rows = 1

sum_negatives = 0
for i in range(first_third_rows):
    for el in qwe[i]:
        if el < 0:
            sum_negatives += el
print(sum_negatives)