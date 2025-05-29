# 1. В двумерном списке найти отрицательные элементы, сформировать из них новый
# массив. Вывести размер полученного массива.
import random
kol_str = random.randint(2,6)
el_in_kol = random.randint(1,6)
qwe = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe)

otr = [el for w in qwe for el in w if el < 0 ]
print(len(otr))



# 2. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов.
averages = [sum(qwe[i]) / len(qwe[i]) for i in range(kol_str) if i % 2 != 0]
print(averages)
