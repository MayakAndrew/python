with open('data.txt', 'x', encoding= 'utf-8') as f:
    """Почему-то моя версия Python 3.10 требует указания кодировки?!
     Иначе текст в кириллице отображается некорректно"""
    while True:
        data = input('Ввод строки - ')
        #data_new = f.write(' ')
        data = f.write(data)
        f.write('\n')
        if not data: break