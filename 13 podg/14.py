
# 1. Для каждого столбца матрицы с четным номером найти сумму ее элементов.
import random
kol_str = random.randint(2,6)
el_in_kol = random.randint(1,6)
qwe = [[random.randint(-100,100) for el in range(el_in_kol)] for w in range(kol_str)]
print(qwe)

sums_even_cols = [sum(qwe[row][col] for row in range(kol_str)) for col in range(el_in_kol) if (col + 1) % 2 == 0]

print(sums_even_cols)

# 2. В двумерном списке найти минимальный элемент в предпоследнем столбце.
