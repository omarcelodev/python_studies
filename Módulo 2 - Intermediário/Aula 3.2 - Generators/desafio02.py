def pares(numeros):
    for n in numeros:
        if n % 2 == 0:
            yield n

def multiplication(numeros):
    for n in pares(numeros):
        yield n * 10
    
for n in multiplication(pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])):
    print(n)