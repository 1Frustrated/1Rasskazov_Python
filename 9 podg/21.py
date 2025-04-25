s = "Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4"
l = s.split()
d = {}
d["оценки"] = []
for w in l[3:]:
    d["оценки"].append(int(w))
s = d["оценки"]
print(sum(s)/len(s))