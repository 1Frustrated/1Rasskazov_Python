# В матрице элементы последней строки заменить на 0.
import random

r = int(input())
n = int(input())

qwe = [[random.randint(9,10) for _ in range(n)] for _ in range(r)]
print(qwe)

for j in range(n):
    qwe[-1][j] = 0
print(qwe)
