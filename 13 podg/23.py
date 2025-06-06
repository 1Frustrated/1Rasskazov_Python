# 1. В двумерном списке найти максимальный положительный элемент, кратный 4.
import random
kol_str = random.randint(2,6)
el_in_kol = random.randint(1,6)
qwe = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe)

ww = [el for w in qwe for el in w if el %4 ==0]
ww = max(ww)
print(ww)




# 2. В двумерном списке все элементы, не лежащие на главной диагонали увеличить в 2
# раза. будет далее
hueta2 = qwe

ww1 = [[qwe[i][j] if i == j else qwe[i][j] * 2 for j in range(el_in_kol)] for i in range(kol_str)]
print(ww1)