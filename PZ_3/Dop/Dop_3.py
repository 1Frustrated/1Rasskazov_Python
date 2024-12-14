try:
    num = int(input("Введите двузначное число: "))
    if num < 10 or num > 99:
        print("Введи двузначное число")
    else:
        sm = (num // 10) + (num % 10)
    if sm % 2 == 0:
        print(num + 2)
    else:
        print(num - 2)
except ValueError:
    print("Введи число")