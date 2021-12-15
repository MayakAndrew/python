class StoreMashines:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

class Printer(StoreMashines):
    def __init__(self, name, price, quantity, speed_print):
        super().__init__(name, price, quantity)
        self.speed_print = speed_print

class Scanner(StoreMashines):
    def __init__(self, name, price, quantity, permission):
        super().__init__(name, price, quantity)
        self.permission = permission

class Copier(StoreMashines):
    def __init__(self, name, price, quantity, chrom):
        super().__init__(name, price, quantity)
        self.chrom = chrom


