def get_numbers(numeros):
    for n in numeros:
        yield n

def filter_pairs(numeros):
    for n in get_numbers(numeros):
        if n % 2 == 0:
            yield n

def return_string(numeros):
    for n in filter_pairs(numeros):
        yield f"Valor: {n}"
    
for n in return_string([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print(n)