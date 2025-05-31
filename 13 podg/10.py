# 1. В двумерном списке элементы третьей строки заменить элементами из одномерного
# динамического массива соответствующей размерности.
import random

kol_str = random.randint(1,6)
el_in_str = random.randint(2,6)

qwe = [[random.randint(-100,100) for el in range(el_in_str)]for w in range(kol_str)]
print(qwe)
qwe11 = [random.randint(-100,100) for el in range(el_in_str)]
print(qwe11)
while True:
    try:
        qwe[2] = qwe11
        break
    except IndexError:
        print("нет 3 строки")
        break

print(qwe)
# 2. В двумерном списке найти среднее арифметическое положительных элементов.

ww = [el for w in qwe for el in w if el > 0]

print(sum(ww)/len(ww))