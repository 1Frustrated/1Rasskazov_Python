# В квадратной матрице элементы на главной диагонали увеличить в 2
# раза.
import random

n = 5  # размер квадратной матрицы

# Генерируем квадратную матрицу n x n с элементами от 1 до 9
matrix = [[random.randint(1, 9) for _ in range(n)] for _ in range(n)]

print("Исходная матрица:")
for row in matrix:
    print(row)

# Увеличиваем элементы главной диагонали в 2 раза
for i in range(n):
    matrix[i][i] *= 2

print("\nМатрица после увеличения элементов главной диагонали в 2 раза:")
for row in matrix:
    print(row)
