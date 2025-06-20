# В матрице элементы первого столбца возвести в куб.

import random

r = int(input())
n = int(input())

qwe = [[random.randint(1,9) for _ in range(n)] for _ in range(r)]
print(qwe)

for i in range(r):
    qwe[i][0] = qwe[i][0] ** 3
print(qwe)