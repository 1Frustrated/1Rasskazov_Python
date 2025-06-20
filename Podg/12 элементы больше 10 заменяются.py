# .Сгенерировать матрицу, в которой элементы больше 10 заменяются на
# 0.

import random

r = int(input())
n = int(input())

qwe = [[random.randint(9,10) for _ in range(n)] for _ in range(r)]
print(qwe)

qwe = [[el if el <10 else 0 for el in row]for row in qwe]
print(qwe)