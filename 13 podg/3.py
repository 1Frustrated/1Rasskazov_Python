# 1. В двумерном списке элементы на главной диагонали увеличить в 2 раза.
import random

kol_str = random.randint(2, 6)       # количество строк
el_in_kol = random.randint(1, 6)     # количество столбцов
qwe = [[random.randint(-100, 100) for el in range(el_in_kol)] for w in range(kol_str)]


ww = [[qwe[q][w] ** 2 if q == w else qwe[q][w] for w in range(el_in_kol)]for q in range(kol_str)]
print(ww)

# 2. Из матрицы сформировать массив из положительных четных элементов, найти их
# сумму и среднее арифметическое.
