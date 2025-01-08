import math


class Figure:
    sides_count = 0  # Атрибут класса Figure: sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)  # Инкапсулированный атрибут объекта (список цветов в формате RGB)
        self.__sides = self.__validate_sides(*sides)  # Инкапсулированный атрибут (список сторон (целые числа))
        self.filled = True  # Публичный атрибут объекта (закрашенный, bool)

    def __validate_sides(self, *sides):  # Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон,
        # возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим,
        # False - во всех остальных случаях.
        if len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides):
            return list(sides)
        return [1] * self.sides_count

    def __is_valid_color(self, r, g, b):  # Метод __is_valid_color - служебный, принимает параметры r, g, b,
        # который проверяет корректность переданных значений перед установкой нового цвета.
        # Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
        return all(0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):  # Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на
        # соответствующие значения, предварительно проверив их на корректность.
        # Если введены некорректные данные, то цвет остаётся прежним.
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):  # Метод get_color, возвращает список RGB цветов.
        return self.__color

    def get_sides(self):  # Метод get_sides должен возвращать значения атрибута __sides.
        return self.__sides

    def __len__(self):  # Метод __len__ должен возвращать периметр фигуры.
        return sum(self.__sides)

    def set_sides(self, *new_sides):  # Метод set_sides(self, *new_sides) должен принимать новые стороны,
        # если их количество не равно sides_count, то не изменять, в противном случае - менять.
        if len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1  # Атрибут класса Circle: sides_count = 1

    # Каждый объект класса Circle должен обладать следующими атрибутами и методами:
    # Все атрибуты и методы класса Figure

    # Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = super().get_sides()[0] / (2 * math.pi)

    # Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3  # Атрибут класса Triangle: sides_count = 3

    # Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
    # Все атрибуты и методы класса Figure

    def get_square(self):  # Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
        a, b, c = super().get_sides()
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure):
    sides_count = 12  # Атрибут класса Cube: sides_count = 12

    # Каждый объект класса Cube должен обладать следующими атрибутами и методами:
    # Все атрибуты и методы класса Figure.

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:  # Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
            super().set_sides(*([sides[0]] * 12))

    def get_volume(self):  # Метод get_volume, возвращает объём куба.
        return super().get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())