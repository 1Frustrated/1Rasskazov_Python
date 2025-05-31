a = open('file.txt', 'r', encoding='utf-8')

r = a.read()
print(r)
z = 0
for i in r:
    if i.isupper():
        z += 1
print(z)

new_lines = []
new_lines.append(r[0])       # первая строка
new_lines.append(r[-1])      # последняя строка
new_lines.extend(r[1:-1])
new_lines = "".join(new_lines)
print(new_lines)

a.close()


