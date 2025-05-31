# 1. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов.
import random
kol_str = random.randint(2,6)
el_in_kol = random.randint(1,6)
qwe = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe)

ww = [sum(qwe[i]) / len(qwe[i]) for i in range(kol_str) if (i + 1) % 2 != 0]
print(ww)



# 2. В двумерном списке найти максимальный положительный элемент, кратный 4.

ww1 = [el for w in qwe for el in w if el % 4 ==0]
ww1 = max(ww1)
print(ww1)