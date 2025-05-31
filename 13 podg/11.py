# 1. В двумерном списке найти сумму и произведение элементов строки N (N задать с
# клавиатуры).


import random
kol_str = random.randint(2,6)
el_in_kol = random.randint(1,6)
qwe = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe)
n = int(input())
ww = sum(qwe[n])

row_product = 1
for val in qwe[n]:
    row_product *= val

print(row_product)

# 2. В двумерном списке найти сумму элементов второй половины матрицы.
hg = kol_str//2
half = qwe[hg:]

print(half)

ww1 = sum([sum(el) for el in half])
print(ww1)