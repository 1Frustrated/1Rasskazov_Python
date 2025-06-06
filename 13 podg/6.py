# 1. В двумерном списке элементы первого столбца возвести в куб.
import random

kol_str = random.randint(2, 6)       # количество строк
el_in_kol = random.randint(1, 6)     # количество столбцов
qwe = [[random.randint(-100, 100) for el in range(el_in_kol)] for w in range(kol_str)]

qwe[0] = [el ** 2 for el in qwe[0]]
print(qwe)

# Сгенерировать двумерный список, в которой элементы больше 10 заменяются на 0.

ww = [[el if el <= 10 else 0 for el in ss] for ss in qwe]
