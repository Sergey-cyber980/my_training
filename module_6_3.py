class Horse:
    def __init__(self):
        self.x_distance = 0  # Пройденный путь
        self.sound = 'Frrr'  # Звук, который издает лошадь

    def run(self, dx):
        self.x_distance += dx  # Увеличение пройденного пути
        print(f"Лошадь пробежала {dx} метров. Общий путь: {self.x_distance} метров.")


class Eagle:
    def __init__(self):
        self.y_distance = 0  # Высота полета
        self.sound = 'Я тренируюсь, ем, сплю и повторяю'  # Звук, который издает орел

    def fly(self, dy):
        self.y_distance += dy  # Увеличение высоты полета
        print(f"Орел поднялся на {dy} метров. Общая высота: {self.y_distance} метров.")


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)  # Инициализация родителя Horse
        Eagle.__init__(self)  # Инициализация родителя Eagle

    def move(self, dx, dy):
        self.run(dx)  # Запуск метода run из класса Horse
        self.fly(dy)  # Запуск метода fly из класса Eagle

    def get_pos(self):
        return (self.x_distance, self.y_distance)  # Текущее положение в виде кортежа

    def voice(self):
        print(self.sound)  # Печать звука, который издает пегас
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
