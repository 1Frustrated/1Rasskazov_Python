# Вариант 16.
# 1. В двумерном списке найти суммы элементов каждой строки и поместить их в новый
# массив. Выполнить замену элементов третьего столбца исходной матрицы на
# полученные суммы.
import random
kol_str = random.randint(2,6)
el_in_kol = random.randint(1,6)
qwe = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe)

ww = [sum(w) for w in qwe]
print(ww)

for i in range(kol_str):
    if el_in_kol >= 3:  # Проверяем, что третий столбец существует
        qwe[i][2] = ww[i]

print(qwe)

# 2. В двумерном списке найти сумму элементов второй половины матрицы
flat_list = [el for row in qwe for el in row]

start_index = len(flat_list) // 2

second_half_elements = flat_list[start_index:]

total_sum = sum(second_half_elements)

print(total_sum)