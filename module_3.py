#Задание_3
name = input('Введите однозначное число:');
name_1 = name + name;
name_2 = name + name + name;
name_int = int(name);
name_1_int = int(name_1);
name_2_int = int(name_2);
name_3 = int(name_int + name_1_int + name_2_int);
print('Сумма:', name_int, '+', name_1_int, '+', name_2_int, '=', name_3);
