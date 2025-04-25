d = {

}
for i in range(7):
    d[i] = i **3

print(d)
s = len(d)
print(s)
del d[s-1]
del d[s-s]
print(d)