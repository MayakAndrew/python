class ComplexNumber:
    def __init__(self, a, b):
        self.a = complex(a)
        self.b = complex(b)
        self.z = a + b

    def __add__(self, other):
        print(f'Сумма a и b равна')
        return f'z = {self.a + self.b}'

    def __mul__(self, other):
        print(f'Произведение a и b равно')
        return f'z = {self.a * self.b}'

    def __str__(self):
        return f'z = {self.a} + {self.b} '

z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)

print(z_1 + z_2)
print(z_1 * z_2)