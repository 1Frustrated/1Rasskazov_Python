class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_gender(self):
        print(f"Пол: {self.gender}")


class Man(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age, gender="Мужчина")

    def show_gender(self):
        print("Пол объекта: Мужчина")


class Woman(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age, gender="Женщина")

    def show_gender(self):
        print("Пол объекта: Женщина")


# ввод данных с клавиатуры
name = input("Введите имя: ")
age = int(input("Введите возраст: "))

# выбор пола
gender_input = input("Введите пол (м/ж): ").strip().lower()

if gender_input == 'м':
    person = Man(name, age)
elif gender_input == 'ж':
    person = Woman(name, age)
else:
    print("Некорректный ввод пола, создаём объект базового класса Person.")
    person = Person(name, age, gender="Не указан")

# вывод информации
print(f"Имя: {person.name}")
print(f"Возраст: {person.age}")
person.show_gender()
