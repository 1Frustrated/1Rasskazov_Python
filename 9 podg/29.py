d = {'a': 1, 'b': 2, 'c': 3, "m": 2, "k": 12}

s = sorted(d.items())
s1 = sorted(d.items(), key=lambda i: i[1])
print(s, s1)
