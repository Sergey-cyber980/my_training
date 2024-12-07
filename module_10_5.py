import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:  # Если строка пустая, выходим из цикла
                break
            all_data.append(line.strip())  # Добавляем строку в список, убирая лишние пробелы
    return all_data  # Возвращаем данные, хотя они не нужны

if __name__ == '__main__':
    # Список названий файлов
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)  # Линейное считывание
    linear_time = time.time() - start_time
    print(f"Линейное время выполнения: {linear_time:.6f} секунд")

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)  # Многопроцессное считывание
    multiprocessing_time = time.time() - start_time
    print(f"Многопроцессное время выполнения: {multiprocessing_time:.6f} секунд")
