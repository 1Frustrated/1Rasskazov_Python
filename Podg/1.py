# Перенести в новую матрицу Matr1 элементы, которые не находятся в
# первых и последних строках и столбцах матрицы Matr2 произвольного
# размера.
import random

kol_str = random.randint(2,8)
el_in_kol = random.randint(2,3)

qwe = [[random.randint(1,3) for _ in range(el_in_kol)] for _ in range(kol_str)]
print(qwe)

if kol_str > 2 and el_in_kol > 2:
    Matr1 = [row[1:-1] for row in qwe[1:-1]]
else:
    Matr1 = []
print(Matr1)
#

