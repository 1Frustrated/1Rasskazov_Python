# 1. В двумерном списке элементы последнего столбца заменить на -1.
import random
kol_str = random.randint(3, 6)
el_in_str = random.randint(2, 4)

hueta = [[random.randint(-100, 100) for _ in range(el_in_str)] for _ in range(kol_str)]

for i in range(kol_str):
    hueta[i][el_in_str - 1] = -1

print(hueta)


# 2. В двумерном списке элементы третьей строки заменить элементами из одномерного
# динамического массива соответствующей размерности
hueta2 = [random.randint(-100, 100) for _ in range(el_in_str)]
print(hueta2)

hueta[2] = hueta2
print(hueta)