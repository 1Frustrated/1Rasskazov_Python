s = "Изучаем язык Питон"
l = s.split()
wc = {}
for w in l:
    if w not in wc:
        wc[w] = 1
    else:
        wc[w] += 1
for key, value in wc.items():
    print(f"{key}: {value}")

