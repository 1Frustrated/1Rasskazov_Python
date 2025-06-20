# 15.В матрице элементы столбца N (N задать с клавиатуры) увеличить в два
# раза.

import random

r = int(input())
n = int(input())

qwe = [[random.randint(9,10) for _ in range(n)] for _ in range(r)]
print(qwe)

n = int(input())
for i in range(r):
    qwe[i][n] *= 2
print(qwe)