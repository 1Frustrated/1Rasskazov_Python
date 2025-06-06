# 1. В двумерном списке элементы последней строки заменить на 0.
# 2. 33 работа
import random

kol_str = random.randint(2,6)
el_in_kol = random.randint(1,6)
qwe = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe)

qwe[kol_str - 1] = [0] * el_in_kol
print(qwe)


# В двумерном списке элементы столбца N (N задать с клавиатуры) увеличить в два
# раза

while True:
    try:
        N = int(input(f"\nВведите номер столбца (от 0 до {el_in_kol - 1}): "))
        if 0 <= N < el_in_kol:
            break
        else:
            print("Номер столбца вне диапазона. Попробуйте снова.")
    except ValueError:
        print("Введите целое число.")

# Увеличиваем элементы столбца N в два раза
for row in qwe:
    row[N] *= 2

print(qwe)