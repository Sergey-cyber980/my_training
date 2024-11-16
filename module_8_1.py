def add_everything_up(a, b):
    try:
        # Проверяем, являются ли оба аргумента числами (int или float)
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b  # Складываем числа
        # Проверяем, являются ли оба аргумента строками
        elif isinstance(a, str) and isinstance(b, str):
            return a + b  # Складываем строки
        else:
            # Если типы разные, вызываем исключение
            raise TypeError("Нельзя складывать разные типы (число и строку).")
    except TypeError:
        # Возвращаем строковое представление обоих аргументов
        return str(a) + str(b)

# Примеры использования
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

print(add_everything_up(5, 10))                  # 15
print(add_everything_up(5.5, 4.5))               # 10.0
print(add_everything_up("Hello, ", "world!"))    # Hello, world!
print(add_everything_up(5, " apples"))            # 5 apples
print(add_everything_up("Count: ", 10))           # Count: 10
