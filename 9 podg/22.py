s = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
l = s.split()
d1 = {}
d1[l[0]] = []
d2 = {}
d2[l[6]] = []
for w in l[1:6]:
    d1[l[0]].append(int(w))
for w in l[7:]:
    d2[l[6]].append(int(w))

r1 = d1[l[0]]
r2 = d2[l[6]]
print(max(r1), max(r2))
