#Даны два целых числа A и B (A < B). Вывести в порядке убывания все целые числа, расположенные между A и B (не включая числа A и B), а также количество N этих чисел.

while True:
    try:
        a = int(input("Введите целое число А: "))
        b = int(input("Введите целое число Б: "))

        if a < b:
            numb = list(range(a + 1, b))
            counter = 0
            for n in reversed(numb):
                print(n, end=" ")
                counter += 1
            print('\nКоличество чисел: ', counter)
            break
        else:
            print("А должно быть меньше Б")

    except ValueError:
        print("Введите 2 целых числа!!!")


