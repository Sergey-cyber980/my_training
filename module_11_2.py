def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not attr.startswith('__') and not callable(getattr(obj, attr))]

    # Получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    # Получаем модуль, к которому принадлежит объект
    obj_module = obj.__class__.__module__  # Исправлено на __class__.__module__

    # Формируем словарь с информацией об объекте
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }

    return info


# Пример использования
number_info = introspection_info(42)
print(number_info)

# Пример для строки
string_info = introspection_info("Hello, World!")
print(string_info)

# Пример для списка
list_info = introspection_info([1, 2, 3, 4])
print(list_info)
