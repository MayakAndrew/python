#Задание_4
per = int(input('Введите число:'));
max = 0;
while True:
   if per > 0:
      end = per % 10;
      per = (per - end) / 10;
      if end >= max:
          max = end;
      else:
          max = max;
   else:
      print('Максимальная цифра в этом числе: ', int(max));
      break;




