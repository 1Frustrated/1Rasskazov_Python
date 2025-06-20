# 6. Из матрицы сформировать массив из положительных четных элементов,
# найти их сумму и среднее арифметическое

import random

kol_str = int(input())
el_in_kol = int(input())

qwe = [[random.randint(1,9) for _ in range(el_in_kol)] for _ in range(kol_str)]
print(qwe)

ww = [el for r in qwe for el in r if el > 0 and el % 2 == 0]
print(sum(ww))
print(sum(ww)/ len(ww))