class Horse:  # Horse - класс описывающий лошадь.
    def __init__(self, *args):
        # Атрибуты класса Horse.
        self.x_distance = 0  # Пройденный путь.
        self.sound = 'Frrr'  # Звук, который издаёт лошадь.
        super().__init__(*args)

    def run(self, dx):  # Метод run(self, dx) увеличивает x_distance на dx.
        self.x_distance += dx


class Eagle:  # Eagle - класс описывающий орла.
    def __init__(self, *args):
        # Атрибуты класса Eagle.
        self.y_distance = 0  # Высота полёта.
        self.sound = 'I train, eat, sleep, and repeat'  # Звук, который издаёт орёл.
        super().__init__(*args)

    def fly(self, dy):  # Метод fly(self, dy) - изменение дистанции, увеличивает y_distance на dy.
        self.y_distance += dy


class Pegasus(Horse, Eagle):  # Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
    def __init__(self, *args):
        super().__init__(*args)  # Инициализируем предков

    # Метод move(self, dx, dy) - где dx и dy изменения дистанции.
    # В этом методе должны запускаться наследованные методы run и fly соответственно.
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    # Метод get_pos(self) возвращает текущее положение пегаса в виде кортежа -
    # (x_distance, y_distance) в том же порядке.
    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):  # Метод voice - печатает значение унаследованного атрибута sound.
        print(self.sound)


# Пример работы программы:
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()