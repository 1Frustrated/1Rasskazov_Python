# Составить программу, в которой функцию построит изображение, в котором в
# первой строке 1 звездочка, во второй - 2, в третьей -3, ..., в строке с номером m - m
# звездочек.
def star(a):
    for i in range(1, a + 1):
        print("*" * i)


try:
    sr = int(input("Ввести число *: "))
    if sr < 0:
        print("Введи положительное число")
except ValueError:
    print("Ввести число *")
star(sr)
