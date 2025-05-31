# 1. В двумерном списке найти среднее арифметическое положительных элементов,
# кратных 3.
import random

kol_str = random.randint(2,6)
el_in_kol = random.randint(1,6)
qwe = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe)

ww = [el for w in qwe for el in w if el % 3 ==0 and el > 0]
print(ww)
print(sum(ww)//len(ww))


# 2. В двумерном списке элементы строки N (N задать с клавиатуры) увеличить на 3.

qwe2 = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe2)
while True:
    try:
        n = int(input(f"Введите номер строки (0..{kol_str - 1}): "))
        if 0 <= n < kol_str:
            break
        else:
            print(f"Номер строки должен быть в диапазоне 0..{kol_str - 1}")
    except ValueError:
        print("Введите целое число")

qwe2[n] = [el + 3 for el in qwe2[n]]
print(qwe2)