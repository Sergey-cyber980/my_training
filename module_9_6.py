def all_variants(text):
    length = len(text)
    # Сначала собираем все подпоследовательности
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield text[start:end]  # Генерируем подпоследовательность

# Пример использования функции
a = all_variants("abc")

# Сначала собираем все результаты в список
results = list(a)

# Сортируем результаты по длине
results.sort(key=len)

# Выводим результаты
for i in results:
    print(i)
