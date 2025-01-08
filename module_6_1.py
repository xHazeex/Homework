
# Создайте 2 класса родителя: Animal, Plant
class Animal:
    # Для класса Animal атрибуты alive = True (живой) и fed = False (не накормленный)
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name  # name - индивидуальное название каждого животного.

    def eat(self, food):  # Метод eat позволяющий им есть растения
        if isinstance(food, Plant):  # Проверяем, является ли еда растением
            if food.edible:  # Если растение съедобное
                print(f"{self.name} съел {food.name}")  # Животное съело растение
                self.fed = True  # Животное накормлено
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False  # Животное погибло из-за несъедобного растения
        else:  # Если еда не является растением
            print(f"{food.name} не является растением. {self.name} не может это съесть.")


class Predator(Animal):  # Класс - наследник Predatar (Хищники) для класса Животных.
    pass


class Mammal(Animal):  # Класс - наследник Mammal (Млекопитающие) для класса Животных.
    pass


class Plant:
    edible = False  # Для класса Plant атрибут edible = False (съедобность)

    def __init__(self, name):
        self.name = name  # name - индивидуальное название каждого растения


class Flower(Plant):  # Класс - наследник Flower (Цветы) для класса Растений.
    edible = False  # Вызываем конструктор родительского класса Plant и устанавливаем, что цветы несъедобные

    def __init__(self, name):
        super().__init__(name)


class Fruit(Plant):  # Класс - наследник Fruit (Фрукты) для класса Растений.
    edible = True  # Вызываем конструктор родительского класса Plant и устанавливаем, что фрукты съедобные

    def __init__(self, name):
        super().__init__(name)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
