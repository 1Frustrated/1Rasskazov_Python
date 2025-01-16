try:
    S = input("Введите строку ")
    S0 = input("Введите подстроку для удаления: ")
    result = S.replace(S0, " ")
    if result == S:
        print("Совпадающих подстрок нет. Строка без изменений:")
    else:
        print("Результирующая строка после удаления подстрок:")
    print(result)
except ValueError:
    print("Неправельно ввели")