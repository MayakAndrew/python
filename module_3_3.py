def my_sum():
    num_1 = int(input('Введите 1-е значение: '));
    num_2 = int(input('Введите 2-е значение: '));
    num_3 = int(input('Введите 3-е значение: '));
    mine = min(num_1, num_2, num_3);
    sume = num_1 + num_2 + num_3;
    sum_max = sume - mine;
    return sum_max;


sum_max = my_sum();
print('Сумма наибольших чисел равна: ', sum_max);




