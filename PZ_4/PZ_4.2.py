n = int(input("Введи положительное число: "))
if n < 0:
    print("Введи положительное число")

k = 0
for k in n:
    if sum(range(1, k)) < n:
        k += 1
    print("jo")

