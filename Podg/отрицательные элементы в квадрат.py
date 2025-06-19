# В матрице отрицательные элементы возвести в квадрат
import random

kol_str = random.randint(2, 8)
el_in_kol = random.randint(2, 8)

qwe = [[random.randint(-9, 9) for _ in range(el_in_kol)] for _ in range(kol_str)]
print("Исходная матрица:")
for row in qwe:
    print(row)

for i in range(kol_str):
    for j in range(el_in_kol):
        if qwe[i][j] < 0:
            qwe[i][j] = qwe[i][j] ** 2

print("\nМатрица после возведения в квадрат отрицательных элементов:")
for row in qwe:
    print(row)
