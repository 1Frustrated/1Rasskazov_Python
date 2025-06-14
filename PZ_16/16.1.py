# 26. Создайте класс «Круг», который имеет атрибут радиуса и методы для вычисления
# площади, длины окружности и диаметра.

class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        "площадь"
        return self.PI * (self.radius ** 2)

    def circumference(self):
        "длина"
        return 2 * self.PI * self.radius

    def diameter(self):
        "диаметр"
        return 2 * self.radius


radius_input = input("Введите радиус круга: ")
radius = float(radius_input)
circle = Circle(radius)

print(f"Радиус: {circle.radius}")
print(f"Площадь: {circle.area()}")
print(f"Длина окружности: {circle.circumference()}")
print(f"Диаметр: {circle.diameter()}")
