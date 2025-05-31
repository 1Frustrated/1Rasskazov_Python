# 1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Элементы первого и второго файлов:
# Элементы первого файла, отсутствующие во втором:
# Элементы второго файла, отсутствующие в первом:
# Количество элементов:
# Индекс первого минимального элемента:
# Индекс последнего максимального элемента:

# файл 1 с положительными и отрицательными числами
import random

forf1 = []
c = random.randint(3,10)
print(c)
for i in range(c):
    n = random.randint(-100, 100)
    forf1.append(n)
    i += 1
sforf1 = " ".join(map(str, forf1))
print(sforf1)


f1 = open('file1.txt', 'w+')
f1.write(sforf1)
f1.close()
# файл 2 с положительными и отрицательными числами
forf2 = []
c2 = 0

while c2 < 20:
    n = random.randint(-100, 100)
    forf2.append(n)
    c2 += 1
sforf2 = " ".join(map(str,forf2))


f2 = open('file2.txt', 'w+')
f2.write(sforf2)
f2.close()

# списки num1 и num2 с эл-тами:

f1 = open('file1.txt', 'r')
content1 = f1.read()
f1.close()
s1 = content1.split()
num1 = []
for p in s1:
    num1.append(int(p))

f2 = open('file2.txt', 'r')
content2 = f2.read()
f2.close()
s2 = content2.split()
num2 = []
for p in s2:
    num2.append(int(p))

#Элементы 1 и 2 файлов:
all_s = num1 + num2
all_str = " ".join(map(str, all_s))

#Элементы первого файла, отсутствующие во втором:
perv1 = set(num1) - set(num2)
perv1 = " ".join(map(str, perv1))

#Элементы второго файла, отсутствующие в первом:
perv2 = set(num2) - set(num1)
perv2 = " ".join(map(str, perv2))

#Количество элементов:
kol_vo = len(all_s)
kol_vo = str(kol_vo)

#Индекс первого минимального элемента:
first_min = min(all_s[:2])
first_min_index = str(all_s.index(first_min))

#Индекс последнего максимального элемента:
last_max = max(all_s[-2:])
last_max_index = str(all_s.index(last_max))


with open('final.txt', 'w', encoding='utf-8') as final:
    final.write('Элементы 1 и 2 файлов:' + all_str + '\n')
    final.write('Элементы первого файла, отсутствующие во втором:' + perv1 + '\n')
    final.write('Элементы второго файла, отсутствующие в первом:' + perv2 + '\n')
    final.write('Количество элементов:' + kol_vo + '\n')
    final.write('Индекс первого минимального элемента:' + first_min_index + '\n')
    final.write('Индекс последнего максимального элемента:' + last_max_index + '\n')
final.close()