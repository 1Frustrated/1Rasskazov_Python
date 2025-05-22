import random

forf1 = []
c = 0

while c < 20:
    n = random.randint(-100, 100)
    forf1.append(n)
    c += 1
sforf1 = " ".join(map(str, forf1))


f1 = open('file1.txt', 'w+')
f1.write(sforf1)
f1.close()
###################################################################################
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
###################################################################################


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
min_index = -1
for i in range(len(all_s)):
    if all_s[i] < all_s[i - 1] or all_s[i] < all_s[i + 1]:
        min_index = i
        break
    elif i == 0:
        if all_s[i] < all_s[i + 1]:
            min_index = i
            break
#Индекс последнего максимального элемента:
max_index = -1
for i in range(len(all_s)):
    if i > 0 and i < len(all_s) - 1:
        if all_s[i] > all_s[i - 1] or all_s[i] > all_s[i + 1]:
            max_index = i
    elif i == len(all_s) - 1:
        if all_s[i] > all_s[i - 1]:
            max_index = i

min_index = str(min_index)
max_index = str(max_index)

with open('final.txt', 'w', encoding='utf-8') as final:
    final.write('Элементы 1 и 2 файлов:' + all_str + '\n')
    final.write('Элементы первого файла, отсутствующие во втором:' + perv1 + '\n')
    final.write('Элементы второго файла, отсутствующие в первом:' + perv2 + '\n')
    final.write('Количество элементов:' + kol_vo + '\n')
    final.write('Индекс первого минимального элемента:' + min_index + '\n')
    final.write('Индекс последнего максимального элемента:' + max_index + '\n')
final.close()