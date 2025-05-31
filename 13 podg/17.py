# 1. Сгенерировать двумерный список на произвольное количество элементов, в которой
# задается преобразование от предыдущего элемента к следующему на произвольное
# значение.
import random
# Генерация случайного количества строк и столбцов
kol_str = random.randint(2, 6)  # Количество строк от 2 до 6
el_in_kol = random.randint(1, 6)  # Количество столбцов от 1 до 6

# Инициализация двумерного списка
qwe = []

# Заполнение списка
for i in range(kol_str):
    row = []
    for j in range(el_in_kol):
        if j == 0:
            # Первое значение в строке - случайное число
            value = random.randint(-100, 100)
        else:
            # Преобразование от предыдущего элемента
            value = row[-1] + random.randint(-10, 10)  # Пример преобразования
        row.append(value)
    qwe.append(row)

print(qwe)
# 2. В двумерном списке найти сумму элементов первых двух строк.
while True:
    try:
        ww = sum([w for w in qwe[0]])
        ww2 = sum([w for w in qwe[1]])

        print(ww + ww2)
        break
    except IndexError:
        print("LL")