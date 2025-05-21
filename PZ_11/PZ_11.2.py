f1 = open('text18-26.txt', 'r', encoding='utf-16')
l = f1.read()
print(l)

t = 0
for el in l:
    if el == "!" or el == '"' or el == "?" or el == "." or el == "," or el == "-" or el == ":" or el == ";" or el == "—":
        t += 1
print(t)

new = ' '
for i in l:
    if i == "!" or i == '"' or i == "?" or i == "." or i == "," or i == "-" or i == ":" or i == ";" or i == "—":
        new += '/'
    else:
        new += i

print(new)
f1.close()
f2 = open('final2.txt', 'w+', encoding='utf-16')
f2.write(new)
f2.close()