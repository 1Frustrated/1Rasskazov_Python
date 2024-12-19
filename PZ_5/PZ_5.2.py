# Описать функцию InvertDigits(K), меняющую порядок следования цифр целого
# положительного числа K на обратный (K — параметр целого типа, являющийся
# одновременно входным и выходным). С помощью этой функции поменять порядок
# следования цифр на обратный для каждого из пяти данных целых чисел.
def InvertDigits(K):
    inv_num = 0
    while K > 0:
        last_num = K % 10
        inv_num = inv_num * 10 + last_num
        K //= 10
    return inv_num


ListAppend = []
i = 0
while i < 5:
    value = int(input('Введи число списка: '))
    ListAppend.append(value)
    i += 1
for num in ListAppend:
    print(InvertDigits(num), end=' ')