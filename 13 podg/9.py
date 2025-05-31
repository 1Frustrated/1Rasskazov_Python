#  В двумерном списке элементы второго столбца заменить элементами из
# одномерного динамического массива соответствующей размерности.

import random

kol_str = random.randint(3, 6)
el_in_str = random.randint(2, 7)

hueta = [[random.randint(-9, 9) for _ in range(el_in_str)] for _ in range(kol_str)]
print(hueta)

ww = [random.randint(-9, 9) for _ in range(kol_str)]
print("\nОдномерный массив для замены второго столбца:")
print(ww)

if el_in_str < 2:
    print("\nВ матрице нет второго столбца для замены.")
else:
    for i in range(kol_str):
        hueta[i][1] = ww[i]

print(hueta)



