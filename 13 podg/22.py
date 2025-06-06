# 1 В двумерном списке найти минимальный элемент в предпоследнем столбце.
import random
kol_str = random.randint(2,6)
el_in_kol = random.randint(1,6)
qwe = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe)
while True:
    try:
        minim = min(row[-2] for row in qwe)
        print(minim)
        break
    except IndexError:
        print("предпоследней строки нет")

# 2. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов.

qwe2 = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe2)


averages = [sum(qwe[i]) / len(qwe[i]) for i in range(kol_str) if (i + 1) % 2 != 0]
index = 1
for avg in averages:
    print(f"Строка {index}: {avg}")
    index += 2