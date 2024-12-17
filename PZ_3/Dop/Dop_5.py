# Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2
try:
    num1 = int(input("Введи число 1: "))
    num2 = int(input("Введи число 2: "))
    if (num2 + num1) % 5 == 0:
        print((num2 + num1) + 1)
    else:
        print((num2 + num1) - 2)
except ValueError:
    print("Введи число")