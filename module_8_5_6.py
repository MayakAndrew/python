class StoreMashines:

    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        print(f'Для выхода - Q, продолжение - Enter')
        while True:
            try:
                unit = input(f'Введите наименование ')
                unit_p = int(input(f'Введите цену за ед '))
                unit_q = int(input(f'Введите количество '))
                unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
                self.my_unit.update(unique)
                self.my_store.append(self.my_unit)
                print(f'Текущий список -\n {self.my_store}')
            except:
                return f'Ошибка ввода данных'
            print(f'Для выхода - Q, продолжение - Enter')
            q = input(f'---> ')
            if q == 'Q' or q == 'q':
                self.my_store_full.append(self.my_store)
                print(f'Весь склад -\n {self.my_store_full}')
                return f'Выход'
            else:
                return StoreMashines.reception(self)

class Printer(StoreMashines):
    def __init__(self, name, price, quantity, speed_print):
        super().__init__(name, price, quantity)
        self.speed_print = speed_print

    def to_print(self):
        return f'принтер {self.speed_print} скорость печати'

class Scanner(StoreMashines):
    def __init__(self, name, price, quantity, permission):
        super().__init__(name, price, quantity)
        self.permission = permission

    def to_scan(self):
        return f'сканер {self.permission} разрешение'

class Copier(StoreMashines):
    def __init__(self, name, price, quantity, chrom):
        super().__init__(name, price, quantity)
        self.chrom = chrom

    def to_copier(self):
        return f'ксерокс {self.self.chrom} четкость'

t = StoreMashines('hp', 2000, 5)
print(t)
r = Scanner('ch', 3000, 4, 10)
print(r.to_scan())