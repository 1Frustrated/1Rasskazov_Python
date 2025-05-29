# 1. Сгенерировать двумерный список, в которой элементы больше 10 заменяются на 0.
import random
kol_str = random.randint(3, 6)
el_in_str = random.randint(2, 4)

hueta = [[random.randint(-100, 100) for _ in range(el_in_str)] for _ in range(kol_str)]
print(hueta)

ww = [[el if el < 10 else 0 for el in w] for w in hueta]

print(ww)

# 2. В двумерном списке все элементы, не лежащие на главной диагонали увеличить в 2
# раза

hueta2 = hueta

ww1 = [[hueta[i][j] if i == j else hueta[i][j] * 2 for j in range(el_in_str)] for i in range(kol_str)]
print(ww1)