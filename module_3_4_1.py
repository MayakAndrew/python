def my_calc():
    a = int(input('Ввод числа А: '))
    b = int(input('Ввод числа В (только отрицательное) '))
    c = abs(b)
    name = []
    i = 0
    d = 1
    while True:
        if i != c:
            name.append(a)
            i += 1
        else:
            break
    for el in name:
        d = (d * el)
    f = (1 / d)
    return f

f = my_calc();
print('Вывод числа a в степени (-b) ', f);






















