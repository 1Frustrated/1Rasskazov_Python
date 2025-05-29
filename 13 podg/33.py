# 1. Из матрицы сформировать массив из положительных четных элементов, найти их
# сумму и среднее арифметическое.
# 2. В двумерном списке найти сумму и произведение элементов столбца N (N задать с
# клавиатуры).
import random
# 111111
kol_kvsk = random.randint(3,5)
el_in_kol = random.randint(4,6)

hueta = [[random.randint(-9, 9) for _ in range(el_in_kol)] for _ in range(kol_kvsk)]
print(hueta)

positive_even = [elem for row in hueta for elem in row if elem > 0 and elem % 2 == 0]

print("\nПоложительные четные элементы:", positive_even)

print(sum(positive_even)//len(positive_even))

#22222222222222
while True:
    try:
        N = int(input(f"\nВведите номер столбца (от 0 до {el_in_kol - 1}): "))
        if 0 <= N < el_in_kol:
            break
        else:
            print("Номер столбца вне диапазона. Попробуйте снова.")
    except ValueError:
        print("Введите целое число.")
column_elements = [row[N] for row in hueta]
sum_column = sum(column_elements)

product_column = 1
for val in column_elements:
    product_column *= val

print(f"Элементы столбца {N}:", column_elements)
print(f"Сумма элементов столбца {N}:", sum_column)
print(f"Произведение элементов столбца {N}:", product_column)
