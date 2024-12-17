# Вести число. Если оно четное, разделить его на 4, если нечетное - умножить на 5
try:
    num = int(input("Введи число "))
    if num % 2 == 0:
        print(num // 4)
    else:
        print(num * 5)
except ValueError:
    print("Введи число")