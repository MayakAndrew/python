num = input('Введите набор слов: ');
num = num.split();
for ing, el in enumerate(num, 1):
    print(ing, el[0:10]);