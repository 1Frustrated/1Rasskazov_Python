import random


def generate_random_list(size):
    return [random.randint(-100, 100) for _ in range(size) if random.randint(-1, 1) != 0]


def check_alternation(numbers):
    if len(numbers) < 2:
        return 0

    previous_sign = 1 if numbers[0] > 0 else -1

    for i in range(1, len(numbers)):
        current_sign = 1 if numbers[i] > 0 else -1
        if current_sign == previous_sign:
            return i + 1
        previous_sign = current_sign
    return 0


try:
    N = int(input("Введите размер списка N: "))
    if N <= 0:
        print("Размер списка должен быть положительным.")
    else:
        numbers = generate_random_list(N)
        print("Сгенерированный список:", numbers)
        result = check_alternation(numbers)
        print(result)
except ValueError:
    print("Пожалуйста, введите корректное целое число.")