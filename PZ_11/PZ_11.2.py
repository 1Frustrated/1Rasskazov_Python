# 2. Из предложенного текстового файла (text18-26.txt) вывести на экран его содержимое,
# количество знаков препинания. Сформировать новый файл, в который поместить текст в
# стихотворной форме предварительно заменив все знаки пунктуации на знак «/».
import string
f1 = open('text18-26.txt', 'r', encoding='utf-16')
l = f1.read()
print(l)

t = 0
for el in l:
    if el in string.punctuation or el == "—":
        t += 1
print(t)

new = ' '
for i in l:
    if i in string.punctuation or i == "—":
        new += '/'
    else:
        new += i

print(new)
f1.close()
f2 = open('final2.txt', 'w+', encoding='utf-16')
f2.write(new)
f2.close()