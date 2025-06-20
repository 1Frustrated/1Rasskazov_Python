# .В матрице элементы строки N (N задать с клавиатуры) увеличить на 3
import random

r = int(input())
n = int(input())

qwe = [[random.randint(9,10) for _ in range(n)] for _ in range(r)]
print(qwe)
n = int(input())
qwe[n] = [el + 3 for el in qwe[n]]
print(qwe)