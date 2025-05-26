# 1.В последовательности их N чисел (N –четное) во второй ее половине найти сумму
# элементов больших 10.
import random
dl = random.choice([i for i in range(10, 21) if i % 2 == 0])
n = [random.randint(1, 100) for i in range(dl)]
print(n)

hf = len(n) // 2
shf = n[hf:]
summa = sum(x for x in shf if x > 10)
print(summa)
