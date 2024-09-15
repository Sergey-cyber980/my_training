my_dict = {'Сергей': 1980, 'Рита': 1985, 'Миша': 1971}
print(my_dict)
print(my_dict['Миша'])
print(my_dict.get('Федя','Такого ключа нет'))
my_dict.update({'Маша': 1990,
                'Дaша': 2000})
print(my_dict)
print(my_dict.pop('Рита'))
print(my_dict)
print()
print('***Работа с множествами:***')
print()
my_set = {2, 4, 3, 5, True, (1, 8,),'Пропеллер'}
print(my_set)
my_set.update([7, 9]) # Добовляем новые элементы в множество
print(my_set)
print(my_set.discard(5))
print(my_set)
