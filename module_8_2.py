class DivisionByNull:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def divide_by_null(a, b):
        try:
            return (a / b)
        except:
            return (f'Деление на ноль недопустимо')

print(DivisionByNull.divide_by_null(10, 0))