# Дан список ненулевых целых чисел размера N. Проверить, чередуются ли в нем
# положительные и отрицательные числа. Если чередуются, то вывести 0, если нет, то
# вывести порядковый номер первого элемента, нарушающего закономерность.
import random
n = int(input("Введи длину списка: "))

spisok = []
i = 0
while i < n:
    spisok.append(random.randint(-100,100))
    i += 1
for i in range(1, len(spisok)):
    if (spisok[i] > 0 and spisok[i - 1] > 0) or (spisok[i] < 0 and spisok[i - 1] < 0):
        print(f"Номер {i + 1} элемент {spisok[i]} не соответствует чередованию.")
        break
else:
    print(0)
print(spisok)