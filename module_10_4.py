import threading
import random
import time
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number  # Номер стола
        self.guest = None  # Гость за столом (по умолчанию None)


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name  # Имя гостя

    def run(self):
        # Ожидание от 3 до 10 секунд
        wait_time = random.randint(3, 10)
        time.sleep(wait_time)
        print(f"{self.name} закончил(-а) приём пищи.")


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()  # Очередь для гостей
        self.tables = tables  # Список столов

    def guest_arrival(self, *guests):
        for guest in guests:
            # Ищем свободный стол
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table:
                free_table.guest = guest  # Сажаем гостя за стол
                guest.start()  # Запускаем поток гостя
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}.")
            else:
                # Если нет свободных столов, помещаем в очередь
                self.queue.put(guest)
                print(f"{guest.name} в очереди.")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла).")
                    print(f"Стол номер {table.number} свободен.")
                    table.guest = None  # Освобождаем стол

                # Если стол свободен и очередь не пуста
                if table.guest is None and not self.queue.empty():
                    guest_from_queue = self.queue.get()
                    table.guest = guest_from_queue
                    guest_from_queue.start()  # Запускаем поток
                    print(f"{guest_from_queue.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}.")

            time.sleep(1)  # Задержка для имитации обслуживания


# Пример использования
if __name__ == "__main__":
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]

    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya',
        'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel',
        'Ilya', 'Alexandra'
    ]

    # Создание гостей
    guests = [Guest(name) for name in guests_names]

    # Заполнение кафе столами
    cafe = Cafe(*tables)

    # Приём гостей
    cafe.guest_arrival(*guests)

    # Обслуживание гостей
    cafe.discuss_guests()

    print("Все гости обслужены.")
