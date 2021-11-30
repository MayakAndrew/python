def fact(n):
    fact = 1
    for num in range(1, n + 1):
        fact *= num
        yield fact
    return fact

for el in fact(5):
    print(el)
