# .Сгенерировать матрицу, в которой нечетные элементы заменяются на 0.

import random

r = int(input())
n = int(input())

qwe = [[random.randint(1,9) for _ in range(n)] for _ in range(r)]
print(qwe)

qwe = [[el if el % 2 == 0 else 0 for el in row] for row in qwe]