"""Обновлённая задача из модуля 5.2"""


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

    def __eq__(self, other):
        return isinstance(other, House) and self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return isinstance(other, House) and self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return isinstance(other, House) and self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return isinstance(other, House) and self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return isinstance(other, House) and self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return isinstance(other, House) and self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h1.go_to(5)
h2.go_to(21)
print()
print("********Решение д/р из модулю 5.2*********")
print()
print("# __str__")
print(h1)
print(h2)
print()
print("# __len__")
print(len(h1))
print(len(h2))
print()
print("********Решение д/р из модулю 5.3*****")
print()
print(h1)
print(h2)
print("# __eq__")
print(h1 == h2)

print("# __add__")
h1 = h1 + 10

print(h1)
print(h1 == h2)

print("# __iadd__")
h1 += (10)
print(h1)
print("# __radd__")
h2 = (10 + h2)
print(h2)
print("# __gt__")
print(h1 > h2)
print("# __ge__")
print(h1 >= h2)
print("# __lt__")
print(h1 < h2)
print("# __le__")
print(h1 <= h2)
print("# __ne__")
print(h1 != h2)
