from itertools import count, islice, filterfalse

def numbers():
    return islice(count(1), 10)

def filter_pairs(numbers):
    return filterfalse(lambda x: x % 2 != 0, numbers)

for n in filter_pairs(numbers()):
    print(f"Valor: {n}")