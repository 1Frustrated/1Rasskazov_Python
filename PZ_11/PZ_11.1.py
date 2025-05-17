import random

forf1 = []
c = 0

while c < 20:
    n = random.randint(-100, 100)
    forf1.append(n)
    c += 1
sforf1 = " ".join(map(str,forf1))
print(sforf1)

f1 = open('file1.txt', 'w+')
f1.write(sforf1)
f1.close()
###################################################################################
forf2 = []
c2 = 0

while c2 < 20:
    n = random.randint(-100, 100)
    forf2.append(n)
    c2 += 1
sforf2 = " ".join(map(str,forf2))
print(sforf2)

f2 = open('file2.txt', 'w+')
f2.write(sforf2)
f2.close()
###################################################################################


f1 = open('file1.txt', 'r')
content1 = f1.read()
f1.close()
s1 = content1.split()
num1 = []
for p in s1:
    num1.append(int(p))

f2 = open('file2.txt', 'r')
content2 = f2.read()
f2.close()
s2 = content2.split()
num2 = []
for p in s2:
    num2.append(int(p))
