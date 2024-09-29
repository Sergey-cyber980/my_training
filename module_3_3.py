# Задача 1: Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовы функции с разным количеством аргументов
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

# Задача 2: Распаковка параметров
values_list = [10, 'Поменянная строка', False]
values_dict = {'a': 5, 'b': 'Есчо какаято строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)

# Задача 3: Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

print("****От себя что нить напишу в качестве закрепления****")

def kakayta_programma(a=1, b='строка', c=True):
     print(a, b, c)



kakayta_programma(a=str("Жаль что выходных мало"))
kakayta_programma(b=("По больше бы по проктиковался"))


