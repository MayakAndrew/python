with open('data_number.txt', 'x', encoding= 'utf-8') as f:
    f.write('2 4 6 8 10 20')
with open('data_number.txt', 'r', encoding= 'utf-8') as f:
    data = f.read()
    data = data.split(' ')
    data = [int(i) for i in data if i != ' ']
    data = sum(data)
    print('Сумма чисел равна: ', data)