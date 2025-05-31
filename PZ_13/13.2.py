# 2. В двумерном списке элементы первого столбца возвести в куб.

import random
kol = random.randint(3, 7)
val = random.randint(2, 5)
sps = [[random.randint(-9, 9) for i in range(val)] for i in range(kol)]
print(sps)

nl = [i[0]**3 for i in sps]
print(nl)

