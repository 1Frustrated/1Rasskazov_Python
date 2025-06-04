# 1. В двумерном списке найти минимальный и максимальные элементы.
import random

kol_str = random.randint(2, 6)       # количество строк
el_in_kol = random.randint(1, 6)     # количество столбцов
qwe = [[random.randint(-100, 100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe)
ww = [min(ss) for ss in qwe]
ww2 = [max(ss) for ss in qwe]
print(min(ww))
print(max(ww2))

# 2. В двумерном списке найти сумму отрицательных элементов в первой трети
# матрицы
first_third_rows = kol_str // 3
if first_third_rows == 0 and kol_str > 0:
    first_third_rows = 1

# Считаем сумму отрицательных элементов в первой трети
sum_negatives = 0
for i in range(first_third_rows):
    for el in qwe[i]:
        if el < 0:
            sum_negatives += el
print(sum_negatives)