#Даны числа x, у. Проверить истинность высказывания: «Точка с координатами (x, у) лежит в четвертой координатной четверти».
try:
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    if x > 0 and y < 0:
        print(f"Точка с координатами {x } { y} расположена в 4 координатной плоскости.")
    else:
        print(f"Точка с координатами {x } { y} не расположена в 4 коордигатной плоскости.")
except ValueError:
    print("Введите целое число")