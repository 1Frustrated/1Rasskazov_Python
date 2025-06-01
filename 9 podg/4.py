d1 = {"a":10, "b":15, "c":12, "d":13, 's': 30, 'e': 40}


def summa():
    val = list(d1.values())
    mid = len(val) // 2
    f1 = sum(val[0:mid])
    f2 = sum(val[mid:])
    print(f1, f2)

summa()



