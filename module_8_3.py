class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения и нажмите Ввод - '))
                self.my_list.append(val)
                print(f'Список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение")
                choice = input(f'Попробовать еще раз? Да/Нет ')

                if choice == 'Да':
                    print(try_except.my_input())
                elif choice == 'Нет' or choice == 'нет':
                    return f'Выход'
                else:
                    return f'Выход'

try_except = Error(1)
print(try_except.my_input())
