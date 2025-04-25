str1 = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
l1 = str1.split()
d1 = {}
d1["апельсины"] = []
d1['яблоки'] = []
for w in l1[1:6]:
    d1["апельсины"].append(int(w))
for w in l1[7:]:
    d1["яблоки"].append(int(w))
r1 = d1["апельсины"]
r2 = d1["яблоки"]
sred1 = sum(r1)//5
sred2 = sum(r2)//5
print(sred1, sred2)
