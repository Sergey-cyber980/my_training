class Vehicle:
    __COLOR_VARIANTS = ['red', 'blue', 'green', 'black', 'white']  # Допустимые цвета

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner  # Владелец транспорта
        self.__model = model  # Модель (марка) транспорта
        self.__engine_power = engine_power  # Мощность двигателя
        self.__color = color  # Цвет автомобиля

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in (color.lower() for color in self.__COLOR_VARIANTS):
            self.__color = new_color
            print(f"Цвет успешно изменен на {new_color}.")
        else:
            print(f"Нельзя сменить цвет на {new_color}.")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # Максимальное количество пассажиров

    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()