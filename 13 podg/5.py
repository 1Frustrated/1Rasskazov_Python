# В двумерном списке элементы второго столбца возвести в квадрат.
import random

kol_str = random.randint(2, 6)       # количество строк
el_in_kol = random.randint(1, 6)     # количество столбцов
qwe = [[random.randint(-100, 100) for el in range(el_in_kol)] for w in range(kol_str)]

qwe[1] = [ss ** 2 for ss in qwe[1]]
print(qwe)


# Сгенерировать двумерный список, в которой нечетные элементы заменяются на 0.
ww = [[el if el%2==0 else 0 for el in ss] for ss in qwe]
print(ww)