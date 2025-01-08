class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}.'

    def __eq__(self, other):  # Метод сравнения на равенство
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):  # Метод сравнения на меньше
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented

    def __le__(self, other):  # Метод сравнения на меньше или равно
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented

    def __gt__(self, other):  # Метод сравнения на больше
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented

    def __ge__(self, other):  # Метод сравнения на больше или равно
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented

    def __ne__(self, other):  # Метод сравнения на неравенство
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return True

    def __add__(self, value):  # Метод сложения для увеличения этажей
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        elif isinstance(value, House):
            return House(self.name, self.number_of_floors + value.number_of_floors)
        return NotImplemented

    def __radd__(self, value):  # Метод обратного сложения (слева от +)
        return self.__add__(value)

    def __iadd__(self, value):  # Метод сложения с присваиванием (+=)
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__