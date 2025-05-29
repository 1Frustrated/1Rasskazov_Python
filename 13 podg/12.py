
# 1. В двумерном списке найти сумму и произведение элементов столбца N (N задать с
# клавиатуры).

import random
kol_str = random.randint(2,6)
el_in_kol = random.randint(1,6)
qwe = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe)

while True:
    try:
        n = int(input(f"Введите номер столбца от 0 до {el_in_kol - 1}: "))
        if 0 <= n < el_in_kol:
            break
        else:
            print(f"Ошибка: номер столбца должен быть от 0 до {el_in_kol - 1}. Попробуйте снова.")
    except ValueError:
        print("Ошибка: введите целое число.")

# Вычисляем сумму и произведение элементов столбца n
col_elements = [qwe[row][n] for row in range(kol_str)]
col_sum = sum(col_elements)

col_product = 1
for val in col_elements:
    col_product *= val

# 2. В двумерном списке найти отрицательные элементы, сформировать из них новый
# массив. Вывести размер полученного массива.