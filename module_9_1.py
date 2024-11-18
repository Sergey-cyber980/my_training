def apply_all_func(int_list, *functions):
    results = {}  # Создаем пустой словарь для хранения результатов

    for func in functions:
        # Проверяем, является ли элемент функцией
        if callable(func):
            results[func.__name__] = func(int_list)  # Вызываем функцию и сохраняем результат

    return results  # Возвращаем словарь с результатами

# Пример использования функции apply_all_func
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
