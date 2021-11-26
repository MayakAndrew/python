def my_segment():
    a = int(input('Введите делимое '));
    b = int(input('Введите делитель '));
    if b == 0:
        print('Ошибка! Деление на ноль невозможно!!!');
    else:
        res = float(a / b);
        print('Результат деление: ', res);

my_segment();
