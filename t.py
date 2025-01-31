str1 = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'
list1 = str1.split()
temperatures = []
for i in list1[1:]:
    temperatures.append(int(i))
temp = {'temperatures': temperatures}
val = temp['temperatures']
minimum = min(val)
sum1 = sum(val)
average_temp = sum1 / len(val)
print(f"Средняя температура: {average_temp}")
print(f"Минимальная температура: {minimum}")
