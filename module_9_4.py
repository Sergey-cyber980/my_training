from random import choice

# 1. Lambda-функция

first = 'Мама мыла раму'
second = 'Рамена мало было'

# Lambda-функция для сравнения символов
compare_chars = lambda f, s: f == s

# Используем map для применения lambda-функции к парам символов из строк
result = list(map(compare_chars, first, second))

print(result)

# 2. Замыкание

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:  # Открываем файл в режиме добавления
            for data in data_set:
                f.write(f"{data}\n")  # Записываем каждое значение в файл
    return write_everything

# Пример использования
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# 3. Метод __call__:

class MysticBall:
    def __init__(self, *words):
        self.words = words  # Сохраняем переданные слова в атрибут

    def __call__(self):
        return choice(self.words)  # Возвращаем случайное слово из списка

# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
