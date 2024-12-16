# Описать функцию InvertDigits(K), меняющую порядок следования цифр целого
# положительного числа K на обратный (K — параметр целого типа, являющийся
# одновременно входным и выходным). С помощью этой функции поменять порядок
# следования цифр на обратный для каждого из пяти данных целых чисел.


def InvertDigits(K):
    return int(str(K)[::-1])


numbers = []
print("Введите 5 целых положительных чисел:")
for i in range(5):
    while True:
        try:
            num = int(input(f"Число {i + 1}: "))
            if num > 0:
                numbers.append(num)
                break
            else:
                print("Пожалуйста, введите положительное целое число.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")


inverted_numbers = [InvertDigits(num) for num in numbers]


print("Инвертированные числа:", inverted_numbers)