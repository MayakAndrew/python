from functools import reduce
def my_func(a, b):
    return a * b
data = [i for i in range(100, 1001, 2)]
print(reduce(my_func, data))