# 1. В двумерном списке элементы строки N (N задать с клавиатуры) увеличить на 3
import random

kol_str = random.randint(2, 6)       # количество строк
el_in_kol = random.randint(1, 6)     # количество столбцов
qwe = [[random.randint(-100, 100) for el in range(el_in_kol)] for w in range(kol_str)]


while True:
    try:
        n = int(input(f"Введите номер строки (0..{kol_str - 1}): "))
        if 0 <= n < kol_str:
            break
        else:
            print(f"Номер строки должен быть в диапазоне 0..{kol_str - 1}")
    except ValueError:
        print("Введите целое число")

qwe[n] = [el + 3 for el in qwe2[n]]
print(qwe)


# 2. В двумерном списке элементы последнего столбца заменить на -1.

for row in qwe:
    row[-1] = -1



