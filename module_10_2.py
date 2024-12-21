import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100  # Количество врагов

    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0

        while self.enemies > 0:
            time.sleep(1)  # Задержка в 1 секунду (1 день)
            days += 1
            self.enemies -= self.power

            # Убедимся, что количество врагов не становится отрицательным
            if self.enemies < 0:
                self.enemies = 0

            print(f"{self.name} сражается {days}день(дня)..., осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


# Создание рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print("Все битвы закончились!")