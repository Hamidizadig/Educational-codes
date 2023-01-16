class Product:
    def __init__(self, productCode, productName, price, color):
        self.productCode = productCode
        self.productName = productName
        self.price = price
        self.color = color

    def showProductInfo(self):
        print(
            f'Code : {self.productCode}\tName : {self.productName}\tPrice : {self.price}')
# -------------------------------------------------


class Clothing(Product):
    def __init__(self, productCode, productName, price, size, color):
        super().__init__(productCode, productName, price, color)
        self.size = size
        # self.color = color

    def __str__(self):
        return f'Code : {self.productCode}\tName : {self.productName}\tPrice : {self.price}\t Size{self.size}\t Color{self.color}'
# --------------------------------------------------


class Food(Product):
    def __init__(self, productCode, productName, price, expirationDate, color='no Color'):
        super().__init__(productCode, productName, price, color)
        self.expirationDate = expirationDate

    def __str__(self):
        return f'Code : {self.productCode}\tName : {self.productName}\tPrice : {self.price}\t expirationDate :{self.expirationDate}\tColor :{self.color}'
# ---------------------------------------------------


class Appliances(Product):
    def __init__(self, productCode, productName, price, brand, model, color):
        super().__init__(productCode, productName, price, color)
        self.brand = brand
        self.model = model
        # self.color = color

    def __str__(self):
        return f'Code : {self.productCode}\tName :{self.productName}\tPrice :{self.price}\t brand :{self.brand}\tmodel :{self.model}\tColor :{self.color}'

    def __del__(self):
        print("**************************************************************************************")


# ---------------------------------------------------
code = int(input('Enter priduct Code : '))
name = input('Enter priduct name : ')
price = int(input('Enter priduct price : '))
brand = input('Enter priduct brand : ')
model = input('Enter priduct model : ')
color = input('Enter priduct color : ')
product5 = Appliances(code, name, price, brand, model, color)
print(product5)
del product5


product1 = Food(1, 'Pfax', 2, '2023-01-20')
product2 = Appliances(20, 'TV', 1825, 'LG', '4982', 'Black')
product3 = Food(2, 'Chips', 2, '2023-03-25', 'Yellow')
product4 = Clothing(1000, 'TShert', 5, 'xxl', 'Blue')

print(product1)
print(product2)
print(product3)
print(product4)

# product1.showProductInfo()

# product2.showProductInfo()
# product3.showProductInfo()
# product4.showProductInfo()
