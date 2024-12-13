try:
    num = int(input("Введи число: "))
    if num > 0:
        print(num + 20)
    else:
        print(num - 5)
except:
    print("Введи число")