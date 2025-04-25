str1 = "Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4"
l = str1.split()
dict1 = {}
dict1[l[0]] = []
for w in l[3:]:
    dict1[l[0]].append(int(w))
print(dict1)
val = dict1[l[0]]
print(val)
al = dict1.values()
print(al)
sred = sum(val)//9
print(sred)



