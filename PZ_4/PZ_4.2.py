# Дано целое число N (> 1). Вывести наибольшее из целых чисел K, для которых сумма
# 1 + 2 + ... + K будет меньше или равна N, и саму эту сумму.

try:
    n = int(input("Введите целое, положительное число: "))
    if n < 0:
        print("Введите положительное число: ")
    s = 0   #сумма
    k = 0   #наибольшее число
    while s+(k+1) <= n:
        k += 1
        s += k
        if s > n:
            break

except ValueError:
    print("Введите число")

print("Сумма чисел равна: ", s)
print("Наибольшее число равно : ", k)