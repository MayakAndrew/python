with open('data.txt', 'r', encoding= 'utf8') as f:
    i = 1
    for line in f.read():
        if line == '\n':
            i += 1
    print('Количество строк в файле: ', i)
e = i
with open('data.txt', 'r', encoding='utf8') as f:
   d = 1
   for d in range(e):
       data = f.readline(d)
       j = 1
       for el in data:
               if el == " ":
                   j += 1
   d += 1
   print(f'Количество слов в строке: {j}')

   """Работает только в части количества слов в последней строке"""
