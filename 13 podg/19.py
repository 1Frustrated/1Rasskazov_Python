# 1. В двумерном списке найти среднее арифметическое элементов последних двух
# столбцов.
import random
kol_str = random.randint(2,6)
el_in_kol = random.randint(1,6)
qwe = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe)

last_two_cols_elements = [row[j] for row in qwe for j in (-2, -1)]
average = sum(last_two_cols_elements) / len(last_two_cols_elements)

# 2. Перенести в новый двумерный список Matr1 элементы, которые не находятся в
# первых и последних сроках и столбцах матрицы Matr2 произвольного размера
import random

# Размеры матрицы
rows = random.randint(3, 6)  # минимум 3, чтобы была внутренняя часть
cols = random.randint(3, 6)

# Создаем матрицу Matr2
Matr2 = [[random.randint(-100, 100) for _ in range(cols)] for _ in range(rows)]

print("Исходная матрица Matr2:")
for row in Matr2:
    print(row)

# Формируем Matr1 — внутренние элементы без крайних строк и столбцов
Matr1 = [row[1:-1] for row in Matr2[1:-1]]

print("\nНовая матрица Matr1 (без первых и последних строк и столбцов):")
for row in Matr1:
    print(row)
