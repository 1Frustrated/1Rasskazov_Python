#
# В двумерном списке найти суммы элементов каждого столбца и поместить их в
# новый массив. Выполнить замену элементов второй строки исходной матрицы на
# полученные суммы
import random
kol_str = random.randint(2,6)
el_in_kol = random.randint(1,6)
qwe = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe)

ww = [sum(row[k] for row in qwe) for k in range(el_in_kol)]
print("\nСуммы по столбцам:")
print(ww)

# Заменяем вторую строку на суммы, если строк больше одной
if kol_str > 1:
    qwe[1] = ww

print(qwe)

# В двумерном списке найти минимальный элемент в предпоследней строке
print(min(qwe[-2]))