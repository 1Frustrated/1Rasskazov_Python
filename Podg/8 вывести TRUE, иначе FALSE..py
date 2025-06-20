# Если в матрице имеются положительные элементы, то вывести TRUE,
# иначе FALSE.
import random

r = int(input())
n = int(input())

qwe = [[random.randint(1,9) for _ in range(n)] for _ in range(r)]
print(qwe)

has_positive = any(elem > 0 for row in qwe for elem in row)

print("TRUE" if has_positive else "FALSE")