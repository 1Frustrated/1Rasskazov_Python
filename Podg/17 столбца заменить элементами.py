# 17.В матрице элементы второго столбца заменить элементами из
# одномерного массива соответствующей размерности.

import random

r = int(input())
n = int(input())

qwe = [[random.randint(9,10) for _ in range(n)] for _ in range(r)]
print(qwe)

ww = [random.randint(9,10) for _ in range(n)]

for i in range(r):
    qwe[i][1] = ww[i]
    
print(qwe)
