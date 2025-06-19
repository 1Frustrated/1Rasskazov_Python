# Перенести в новый двумерный список Matr1 элементы, которые не находятся в
# первых и последних строках и столбцах матрицы Matr2 произвольного размера.
import random

kol_str = random.randint(2, 6)       # количество строк
el_in_kol = random.randint(1, 6)     # количество столбцов
qwe = [[random.randint(-100, 100) for el in range(el_in_kol)] for w in range(kol_str)]


if kol_str <= 2 or el_in_kol <= 2:
    print("\nМатрица слишком мала, чтобы иметь внутренние элементы (без первых и последних строк и столбцов).")
    Matr1 = []
else:
    # Формируем Matr1 из элементов, не лежащих в первых/последних строках и столбцах
    Matr1 = [
        row[1:-1]  # берем элементы со второго до предпоследнего столбца
        for row in qwe[1:-1]  # берем строки со второй до предпоследней
    ]





# 2. В двумерном списке отрицательные элементы возвести в квадрат.

import random

kol_str = random.randint(2, 8)
el_in_kol = random.randint(2, 8)

# Генерация матрицы с элементами от -9 до 9, чтобы были отрицательные числа
qwe = [[random.randint(-9, 9) for _ in range(el_in_kol)] for _ in range(kol_str)]
print("Исходная матрица:")
for row in qwe:
    print(row)

# Возведение в квадрат отрицательных элементов
for i in range(kol_str):
    for j in range(el_in_kol):
        if qwe[i][j] < 0:
            qwe[i][j] = qwe[i][j] ** 2

print("\nМатрица после возведения в квадрат отрицательных элементов:")
for row in qwe:
    print(row)

