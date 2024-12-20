class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        str_product = f'{self.name}, {self.weight}, {self.category}'
        return  str_product

class Shop:
    __file_name = 'products.txt'
    def get_product(self):
        file = open(self.__file_name, 'r')
        prod_str = file.read()
        file.close()
        return prod_str

    def add(self, *products):
        products_in_file = self.get_product()
        file = open(self.__file_name, 'a')
        for product in products:
            if str(product) not in products_in_file:
                file.write(f'{product}\n')
            else:
                print(f'Продукт {product} уже есть в магазине')
                file.close()

# Пример использования
if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_product())
