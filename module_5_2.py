"""Обновлённая задача из модуля 5.1"""


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f"Tакого этажа не существует {new_floor}")
        else:
            for floor in range(1, new_floor + 1):
                print(f"Подымаемся на этаж {floor}")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


h1 = House('ЖК Горский', 10)
h2 = House('ЖК Акация', 20)
h1.go_to(5)
h2.go_to(21)
print()
print("*********************************")
print()
print("# __str__")
print(h1)
print(h2)
print()
print("# __len__")
print(len(h1))
print(len(h2))
