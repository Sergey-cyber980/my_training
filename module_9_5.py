class StepValueError(ValueError):
    """Исключение для некорректного значения шага."""
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        # Проверяем, что step не равен 0
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')

        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start  # Устанавливаем указатель на начальное значение

    def __iter__(self):
        self.pointer = self.start  # Сбрасываем указатель на start
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration  # Завершаем итерацию, если указатель вышел за пределы

        current_value = self.pointer
        self.pointer += self.step  # Увеличиваем указатель на шаг
        return current_value


# Примеры использования
try:
    iter1 = Iterator(100, 200, 0)  # Это вызовет исключение
    for i in iter1:
        print(i, end=' ')
except StepValueError as e:
    print('Шаг указан неверно:', e)

# Создаем другие итераторы
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

# Итерация по iter2
for i in iter2:
    print(i, end=' ')
print()

# Итерация по iter3
for i in iter3:
    print(i, end=' ')
print()

# Итерация по iter4
for i in iter4:
    print(i, end=' ')
print()

# Итерация по iter5
for i in iter5:
    print(i, end=' ')
print()
