# В матрице найти минимальный и максимальные элементы.

import random

kol_str = random.randint(2,8)
el_in_kol = random.randint(2,8)

qwe = [[random.randint(1,9) for _ in range(el_in_kol)] for _ in range(kol_str)]
print(qwe)

ww = [min(ss) for ss in qwe]
print(ww)
ww2 = [max(ss) for ss in qwe]
print(ww2)
print(min(ww))
print(max(ww2))