import random
N = int(input("Введите размер списка A (менее 15): "))
if N >= 15:
    print("Размер списка должен быть меньше 15.")
else:
    spisok = []
    i = 0
    while i < N:
        spisok.append(random.randint(-100,100))
        i += 1
    sec_spisok = spisok[1::2]
    print("Сгенерированный список A:", spisok)
    print("Размер списка B:", len(sec_spisok))
    print("Содержимое списка B:", sec_spisok)
