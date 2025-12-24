def pares(numeros):
    for n in numeros:
        if n % 2 == 0:
            yield n

for n in pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print(n)