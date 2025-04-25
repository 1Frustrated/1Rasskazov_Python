s = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'
l = s.split()
d = {}
d[l[0]] = []
for w in l[1:]:
    d[l[0]].append(int(w))
a = d[l[0]]
sr = sum(a)/12
print(sr)