#Даны числа x, у. Проверить истинность высказывания: «Точка с координатами (x, у) лежит в четвертой координатной четверти».
try:
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    if x > 0 and y < 0:
        print("True")
    else:
        print("False")
except ValueError:
    print("Введите число")
