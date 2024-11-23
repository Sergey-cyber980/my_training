# Данные списки
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Список длин строк из first_strings, где длина строк не менее 5 символов
first_result = [len(string) for string in first_strings if len(string) >= 5]

# 2. Список пар слов (кортежей) одинаковой длины
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# 3. Словарь, где ключ - строка, значение - длина строки (только для четной длины)
third_result = {string: len(string) for string in first_strings + second_strings if len(string) % 2 == 0}

# Пример выполнения кода:
print(first_result)
print(second_result)
print(third_result)
