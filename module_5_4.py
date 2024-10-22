# Дополнительно о работе метода __new__:


class StrVremPi:
    data = (0)  # 'data' будет находиться под индексом 0

    def __new__(cls, *args, **kwargs):
        print("Метод new:")
        data = args  # 'data' в *args: ('data',)
        second = kwargs  # 'second' в **kwargs: 25
        third = kwargs  # 'third' в **kwargs: 3.14
        return super(StrVremPi, cls).__new__(cls)

    def __init__(self, first, second, third):
        print("Передача данных из new в init:")
        print(f"Параметр first: {first}")
        print(f"Параметр second: {second}")
        print(f"Параметр third: {third}")


# Создание объекта класса House с передачей аргументов
my_house = StrVremPi('data', second=25, third=3.14)

print('******************************')

# Задача "История строительства":

class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        house_name = args[0]
        cls.houses_history.append(house_name)
        return super(House, cls).__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

