# Дана строка '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15', отражающая
# средние температуры по месяцам в году. Преобразовать информацию из строки в
# словарь, с использованием функции найти среднюю и минимальные температуры.,
# результаты вывести на экран..
str1 = "2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15"
d1 = {}
spl = str1.split()
del spl[0]
d1["temperature"] = []
for value in spl:
    d1["temperature"].append(int(value))
z = d1["temperature"]
minimum = min(z)
sred = sum(z)/12
print(minimum, sred)






