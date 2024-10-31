class Animal:
    def __init__(self, name):
        self.alive = True  # Живое
        self.fed = False   # Накормленное
        self.name = name   # Имя животного

    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f"{self.name} съел {food.name}.")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name} и погиб.")

class Plant:
    def __init__(self, name):
        self.edible = False  # Съедобность
        self.name = name      # Имя растения

class Mammal(Animal):
    pass  # Млекопитающие могут использовать метод eat из Animal

class Predator(Animal):
    pass  # Хищники могут использовать метод eat из Animal

class Flower(Plant):
    pass  # Цветы по умолчанию не съедобные

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Плоды съедобные

# Создание объектов классов
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
