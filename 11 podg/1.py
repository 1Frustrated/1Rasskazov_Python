f1 = open('text18-26.txt', 'r', encoding='utf-16')

read = f1.read()
print(read)
f1.close()
i = 0
for w in read:
    if w.isupper():
        i += 1
print(i)

f1 = open('text18-26.txt', 'r', encoding='utf-16')
rl = f1.readlines()
f1.close()

last_line = rl.pop(-1)  
rl.insert(1, last_line)
print(rl)
