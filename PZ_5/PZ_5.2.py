# Описать функцию InvertDigits(K), меняющую порядок следования цифр целого
# положительного числа K на обратный (K — параметр целого типа, являющийся
# одновременно входным и выходным). С помощью этой функции поменять порядок
# следования цифр на обратный для каждого из пяти данных целых чисел.
def InvertDigits(K):
    K = str(K)[::-1]
    return K


ListAppend = []
i = 0
while i < 5:
    value = int(input('Введи число списка: '))
    ListAppend.append(value)
    i += 1
for num in ListAppend:
    inv_num = InvertDigits(num)
    print(inv_num, end=' ')