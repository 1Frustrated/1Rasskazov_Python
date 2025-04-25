s = "Изучаем язык Питон"
s = s.lower()
l = s.split()
d = {}
for w in l:
    if w not in d:
        d[w] = 1
    else:
        d[w] +=1

print(d)