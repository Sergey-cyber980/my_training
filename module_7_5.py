import os
import time

directory = "."

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file) # Формируем полный путь к файлу

        filetime = os.path.getmtime(filepath) # Получаем время последнего изменения файла

        # Форматируем время
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получаем размер файла
        filesize = os.path.getsize(filepath)

        # Получаем родительскую директорию файла
        parent_dir = os.path.dirname(filepath)

        # Выводим информацию о файле
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')