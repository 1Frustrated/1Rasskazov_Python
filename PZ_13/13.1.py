# В двумерном списке найти среднее арифметическое положительных элементов.

import random
kol = random.randint(3, 7)
val = random.randint(2, 5)
sps = [[random.randint(-9, 9) for i in range(val)] for i in range(kol)]
print(sps)



el = [print(e) for e in sps]
pe = [num for el in sps for num in el if num > 0]
print(pe)

summa = sum(pe)

print(summa // len(pe))
