import math

class Figure:
    sides_count = 0  # Количество сторон (атрибут класса)

    def __init__(self, sides, color):
        # Проверка на количество сторон
        if len(sides) != self.sides_count:
            sides = [1] * self.sides_count  # Создаем массив с единичными сторонами
        self.__sides = sides  # Инкапсулированный атрибут: список сторон
        self.__color = color  # Инкапсулированный атрибут: список цветов в формате RGB
        self.filled = False  # Публичный атрибут: закрашенный

    def get_color(self):
        """Возвращает список RGB цветов."""
        return self.__color

    def __is_valid_color(self, r, g, b):
        """Проверяет корректность переданных значений цвета."""
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        """Устанавливает новый цвет, если он корректен."""
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        else:
            print("Вводим цвета.")

    def __is_valid_sides(self, *new_sides):
        """Проверяет корректность новых сторон."""
        if len(new_sides) != self.sides_count:
            return False
        return all(isinstance(side, (int, float)) and side > 0 for side in new_sides)

    def get_sides(self):
        """Возвращает список сторон."""
        return self.__sides

    def __len__(self):
        """Возвращает периметр фигуры."""
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        """Устанавливает новые стороны, если количество совпадает с sides_count."""
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides
        else:
            print("Вводим стороны.")

class Circle(Figure):
    sides_count = 1  # Количество сторон для круга

    def __init__(self, color, circumference):
        radius = circumference / (2 * math.pi)  # Рассчитываем радиус по длине окружности
        super().__init__([circumference], color)  # Передаем длину окружности как единственную сторону
        self.__radius = radius  # Инкапсулированный атрибут: радиус

    def get_square(self):
        """Возвращает площадь круга."""
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3  # Количество сторон для треугольника

    def __init__(self, color, a=1, b=1, c=1):
        super().__init__([a, b, c], color)  # Передаем стороны треугольника

    def get_square(self):
        """Возвращает площадь треугольника по формуле Герона."""
        s = sum(self.get_sides()) / 2  # Полупериметр
        return math.sqrt(s * (s - self.get_sides()[0]) * (s - self.get_sides()[1]) * (s - self.get_sides()[2]))

class Cube(Figure):
    sides_count = 12  # Количество сторон для куба

    def __init__(self, color, side_length=1):
        sides = [side_length] * 12  # 12 одинаковых сторон
        super().__init__(sides, color)  # Передаем стороны куба

    def get_volume(self):
        """Возвращает объем куба."""
        return self.get_sides()[0] ** 3  # Объем = длина стороны в кубе

# Пример использования
if __name__ == "__main__":
    # Создание объектов
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