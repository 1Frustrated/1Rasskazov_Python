d = {'a': 1, 'b': 2, 'h': 5, 'c': 3}
s = sorted(d)
print(s)
s1 = d.values()
for w in s:
    if d[w] >= 1:
        print(f"{w}: {d[w]}")