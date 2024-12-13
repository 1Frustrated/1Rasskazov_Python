try:
    num1 = int(input("Введи число 1: "))
    num2 = int(input("Введи число 2: "))
    if (num2 + num1) % 5 == 0:
        print((num2 + num1) + 1)
    else:
        print((num2 + num1) - 2)
except ValueError:
    print("Введи число")