class Textil:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_j(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Общая площадь ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')

class Coat(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = self.width / 6.5 + 0.5

    def __str__(self):
        return f'Площадь на пальто {self.square_c}'

class Jacket(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = self.height * 2 + 0.3

    def __str__(self):
        return f'Площадь на костюм {self.square_j}'

coat = Coat(1, 4)
jacket = Jacket(1, 2)
print(coat)
print(jacket)
print(jacket.get_sq_full)