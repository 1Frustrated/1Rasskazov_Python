# .В матрице найти среднее арифметическое положительных элементов,
# кратных 3.

import random

r = int(input())
n = int(input())

qwe = [[random.randint(-1,6) for _ in range(n)] for _ in range(r)]
print(qwe)

w = [el for row in qwe for el in row if el > 0 and el % 3 == 0]

print(sum(w)/len(w))