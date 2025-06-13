class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        "Вычисление площади круга"
        return self.PI * (self.radius ** 2)

    def circumference(self):
        "Вычисление длины окружности"
        return 2 * self.PI * self.radius

    def diameter(self):
        "Вычисление диаметра круга"
        return 2 * self.radius


radius_input = input("Введите радиус круга: ")

radius = float(radius_input)

circle = Circle(radius)

print(f"Радиус: {circle.radius}")
print(f"Площадь: {circle.area():.2f}")
print(f"Длина окружности: {circle.circumference():.2f}")
print(f"Диаметр: {circle.diameter()}")
