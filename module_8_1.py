def add_everything_up(a, b):
    try:
        # Проверяем, являются ли оба аргумента числами (int или float)*
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b 
        elif isinstance(a, str) and isinstance(b, str):
            return a + b  
        else:    
            raise TypeError("Нельзя складывать разные типы (число и строку).")
    except TypeError:
       return str(a) + str(b)

# Примеры использования
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

print(add_everything_up(5, 10))                  
print(add_everything_up(5.5, 4.5))               
print(add_everything_up("Hello, ", "world!"))    
print(add_everything_up(5, " apples"))       
print(add_everything_up("Count: ", 10))      
