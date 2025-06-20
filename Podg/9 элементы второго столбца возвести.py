# 9. В матрице элементы второго столбца возвести в квадрат
import random

r = int(input())
n = int(input())

qwe = [[random.randint(1,9) for _ in range(n)] for _ in range(r)]
print(qwe)

qwe[1] = [el ** 2 for el in qwe[1]]
print(qwe)