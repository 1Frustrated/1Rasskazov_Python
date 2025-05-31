import random
from functools import reduce
kol = random.choice([e for e in range(5,15)])   #Количество элементов
elements = [random.randint(-100,100) for e in range(kol)]
print(elements)

# Исходные данные:
all_elements = elements

# Отрицательные нечетные элементы:
otr_n = [e for e in elements if e % 2 != 0 and e <0]

# Сумма отрицательных нечетных элементов:
sum_otr_n = sum(otr_n)

# Среднее арифметическое отрицательных нечетных элементов:
sred = sum_otr_n // kol

# Максимальный элемент:
maxi = str(max(all_elements))

# Произведение элементов меньших 0 в первой половине:
polovina = len(elements)//2
polovina_otr = [s for s in elements[:polovina] if s < 0]
fmult = 1
proizv = str(reduce(lambda x, y: x * y, polovina_otr, 1))
# 2 вариант
# polovina_otr = [-2, -1, -3]
# proizv = 1
# for num in polovina_otr:
#     proizv *= num
# print(proizv)  # Результат: -6


# Квадраты четных элементов:
kv_chet = [s**2 for s in all_elements if s%2 ==0]

# Сумма квадратов четных элементов:
summa_kv_chet = sum(kv_chet)

# Элементы, умноженные на первый максимальный элемент:
first_max = max(elements[:2])
elements_mult_max = str([x * first_max for x in elements])

# Повторяющиеся элементы:
unique = []
repeats = []

for num in elements:
    if num in unique:
        if num not in repeats:
            repeats.append(num)
    else:
        unique.append(num)

print(repeats)
# Количество повторяющихся элементов:
print(len(repeats))
# Произведение элементов:
print(reduce(lambda a, b : a * b, elements))
n = 1
for el in elements:
    n *= el
print(n)

# Положительные четные элементы:
pol_chet_el = [s for s in elements if s > 0 and s % 2 == 0]
print(pol_chet_el)

#срез 2х послед эл-тов
print(elements[-2:])

# Меняем местами первую и последнюю трети
tret = len(elements)//3
print(tret)
first_third = elements[:tret]
middle = elements[tret:-tret]
last_third = elements[-tret:]
swap = last_third + middle + first_third

#reverse
print(elements[::-1])

# Количество пар, для которых произведение элементов делится на 3 (элементы пары в
# последовательности являются соседними):

count = 0
for i in range(len(elements) - 1):
    if (elements[i] * elements[i + 1]) % 3 == 0:
        count += 1
print(count)

# Последовательность, в которой каждый последующий элемент равен квадрату суммы двух
# соседних элементов
old_elements = elements.copy()
for i in range(1, len(elements) - 1):
    elements[i] = (old_elements[i - 1] + old_elements[i + 1]) ** 2
    s = elements[i]
    print(s)


# преобразование
all_elements = ' '.join(map(str, all_elements))
kol = str(kol)
otr_n = ' '.join(map(str, otr_n))
sum_otr_n = str(sum_otr_n)
sred = str(sred)
kv_chet = str(kv_chet)
summa_kv_chet = str(summa_kv_chet)



#ответ
with open('file.txt', 'w+', encoding='utf-8') as f:
    f.write("Исходные данные:" + all_elements + "\n")
    f.write("Длина:" + kol + "\n")
    f.write("Отрицательные нечетные элементы:" + otr_n + "\n")
    f.write("Сумма отрицательных нечетных элементов:" + sum_otr_n + "\n")
    f.write("Среднее арифметическое отрицательных нечетных элементов:" + sred + "\n")
    f.write("Максимальный элемент:" + maxi + "\n")
    f.write("Произведение элементов меньших 0 в первой половине:" + proizv + "\n")
    f.write("Квадраты четных элементов:" + kv_chet + "\n")
    f.write("Сумма квадратов четных элементов:" + summa_kv_chet + "\n")
    f.write("Элементы, умноженные на первый максимальный элемент:" + elements_mult_max + "\n")
    f.write("Элементы, умноженные на первый максимальный элемент:" + summa_kv_chet + "\n")
