dict = {}
with open('spisok.txt', 'r', encoding= 'utf-8') as f:
    data = f.read()
    data = data.split('\n')
for item in data:
    key = item.split(" ")[0]
    value = item.split(" ")[1:]
    dict[key] = value
    print(dict)
    """Дальше вывода в словарь решить задачу не смог.
    Нужно позаниматься разделом Словарь"""

