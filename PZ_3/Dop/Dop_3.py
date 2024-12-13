try:
    num = int(input("Введите двузначное число: "))
    if num < 10 or num > 99:
        print("Введи двузначное число")
    else:
        num = str
        print(sum(num[0] + num[1]))
except ValueError:
    print("Введите число")