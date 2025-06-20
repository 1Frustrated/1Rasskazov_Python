# В матрице элементы последнего столбца заменить на -1.
import random

r = int(input())
n = int(input())

qwe = [[random.randint(9,10) for _ in range(n)] for _ in range(r)]
print(qwe)

for i in range(r):
    qwe[i][-1] = -1
print(qwe)