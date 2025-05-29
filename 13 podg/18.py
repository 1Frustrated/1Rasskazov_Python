# 1. В двумерном списке элементы кратные 3 увеличить в 3 раза.
import random
kol_str = random.randint(2,6)
el_in_kol = random.randint(1,6)
qwe = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe)

ww = [el * 3 if el % 3 == 0 else el for w in qwe for el in w]
print(ww)


# 2. В двумерном списке найти среднее арифметическое элементов последних двух
# столбцов.

last_two_cols_elements = [row[j] for row in qwe for j in (-2, -1)]
average = sum(last_two_cols_elements) / len(last_two_cols_elements)