#Задание_5
proceeds = int(input('Введите значение выручки за период, руб.:'));
costs = int(input('Введите значение издержек за период, руб.:'));
profit = int(proceeds - costs);
if profit > 0:
    print('Прибыль составила: ', profit, 'руб.');
    rent = int(profit / costs * 100);
    print('Рентабельность составила:', rent, '%');
    staff = int(input('Сообщите численность персонала, чел.: '));
    profit_staff = int(profit / staff);
    print('Прибыль в расчете на одного работника составила:', profit_staff, 'руб.');
else:
    print('Работа с убытком', profit, 'руб.');