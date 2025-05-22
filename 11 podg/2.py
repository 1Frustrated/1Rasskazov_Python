f1 = open('text18-26.txt', 'r', encoding='utf-16')

read = f1.read()
print(len(read))
i = 0
for w in read:
    if w != " ":
        i+=1
print(i)
f1.close()



