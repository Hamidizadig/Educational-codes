class Test:
    def __init__(self):
        self.list1=[]
    def addProduct(self,product):
        self.list1.append(product)
    def showList(self):
        for product in self.list1:
            for key,value in product.items():
                print(key,value)
t1=Test()
t1.addProduct({'Name':'CPU','Price':120000})
t1.addProduct({'Name':'CPU','Price':89000})
t1.showList()
