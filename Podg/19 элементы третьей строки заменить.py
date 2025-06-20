# В матрице элементы третьей строки заменить элементами из
# одномерного массива соответствующей размерности.

import random

r = int(input())
n = int(input())

qwe = [[random.randint(-1,6) for _ in range(n)] for _ in range(r)]
print(qwe)

w = [random.randint(-1,6) for _ in range(n)]
print(w)

for i in range(n):
    qwe[2][i] = w[i]

print(qwe)