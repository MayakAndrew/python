with open('data_new.txt', 'r', encoding= 'utf-8') as f:
    data = f.readline()
    with open('data_one.txt', 'a', encoding= 'utf-8') as d:
        data_new = data.replace('One', 'Один')
        data = d.write(data_new)
        data = f.readline()
        data_new = data.replace('Two', 'Два')
        data = d.write(data_new)
        data = f.readline()
        data_new = data.replace('Three', 'Три')
        data = d.write(data_new)
        data = f.readline()
        data_new = data.replace('Four', 'Четыре')
        data = d.write(data_new)
"""Решение очень не рациональное, можно сказать передернутое"""