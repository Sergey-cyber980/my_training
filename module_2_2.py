first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

if first == second == third:
    print("Вывод на консоль число: 3")
elif first == second or first == third or second == third:
    print("Вывод на консоль число: 2")
else:
    print("Вывод на консоль число: 0")
