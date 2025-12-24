def quadrado_pares(numeros):
    for n in numeros:
        if n % 2 == 0:
            yield n ** 2

for n in quadrado_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print(n)