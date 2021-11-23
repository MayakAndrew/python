#Задание_2
import datetime
sec = int(input('Введите количество времени в секундах: '));
hour = int((sec // 3600));
minut = int((sec - hour * 3600) // 60);
sec_1 = int(sec - hour * 3600 - minut * 60);
a = datetime.time(hour, minut, sec_1);
print(a);