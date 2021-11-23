# Задание_6
distance = float(input('Введите длину дистанции в первый день:'));
result = float(input('Введите жедаемый результат:'));
counter_days = 1;
while True:
    distance = distance * 1.1;
    if distance < result:
        counter_days = counter_days + 1;
    else:
        counter_days = counter_days + 1;
        print('На', counter_days, '-й день результат будет достигнут');
        break;
