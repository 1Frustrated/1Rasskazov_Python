
# 1. Если в двумерном списке имеются положительные элементы, то вывести TRUE,
# иначе FALSE.


import random

kol_str = random.randint(3, 6)
el_in_str = random.randint(4, 7)

hueta = [[random.randint(-9, 9) for _ in range(el_in_str)] for _ in range(kol_str)]
print(hueta)

has_positive = any(elem > 0 for row in hueta for elem in row)

print("TRUE" if has_positive else "FALSE")

# 2. В двумерном списке найти сумму и произведение элементов строки N (N задать с
# клавиатуры).

kol_str = random.randint(3, 6)
el_in_str = random.randint(4, 7)
while True:
    try:
        n = int(input())
        if 0 <= n < kol_str:
            break
        else:
            print(f"n не в диапазоне {kol_str}")
    except:
        print("введи число")

row_elements = hueta[n]
sum_row = sum(row_elements)

product_row = 1
for val in row_elements:
    product_row *= val

print(product_row)