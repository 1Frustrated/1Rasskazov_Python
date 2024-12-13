# Ввести 2 числа. Если их произведение отрицательно, умножить его на 8, в противном
# случае увеличить его в 1.5 раза.
try:
    num1 = int(input("Введите число 1: "))
    num2 = int(input("Введите число 2: "))
    if num1 * num2 < 0:
        print(num1 * num2 * 8)
    else:
        print(num1 * num2 * 1.5)
except ValueError:
    print("Введите число")