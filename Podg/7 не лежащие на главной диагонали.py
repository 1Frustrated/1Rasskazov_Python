# . В квадратной матрице все элементы, не лежащие на главной диагонали
# увеличить в 2 раза.
import random

r = int(input())


qwe = [[random.randint(1,9) for _ in range(r)] for _ in range(r)]
print(qwe)

qwe = [[qwe[e][j] if e==j else qwe[e][j]**2 for j in range(r)] for e in range(r)]
print(qwe)