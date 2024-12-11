#Даны два целых числа A и B (A < B). Вывести в порядке убывания все целые числа, расположенные между A и B (не включая числа A и B), а также количество N этих чисел.

try:
    a = int(input("Введите целое число А "))
    b = int(input("Введите целое число Б "))
    if a < b:
        counter = 0
        numb = list(range(a + 1, b))
        for n in reversed(numb):
            print(n, end=" ")
            counter += 1
        print('Количество чисел: ', counter)
    else:
        print("А должно быть меньше Б")
except ValueError:
    print("Введите 2 целых числа!!!")

