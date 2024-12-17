import random
def check(a):
    f = None
    for i in range(len(a)):
        if f is None:
            f = a[i] < 0
        elif (a[i] > 0) == f:
            f = not f
        else:
            return i + 1
    return 0


a = [random.randint(-10, 10) for _ in range(10)]
print(a)
print(check(a))