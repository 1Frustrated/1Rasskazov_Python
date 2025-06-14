import random
# Вариант 25.
# 1. В двумерном списке найти сумму элементов второй половины матрицы.
kol_str = random.randint(2,6)
el_in_kol = random.randint(1,6)
qwe = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe)

flat_list = [el for row in qwe for el in row]

start_index = len(flat_list) // 2

second_half_elements = flat_list[start_index:]

total_sum = sum(second_half_elements)

print(total_sum)


# 2. В двумерном списке элементы второго столбца возвести в квадрат.

qwe[1] = [el ** 2 for el in qwe[1]]
print(qwe)