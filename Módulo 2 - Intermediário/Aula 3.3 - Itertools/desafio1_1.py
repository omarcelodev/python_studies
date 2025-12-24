from itertools import count, islice, filterfalse

def number_generator():
    for n in count(1):
        yield n

def get_numbers():
    for n in islice(number_generator(), 10):
        yield n

def filter_pairs():
    nums = []

    for n in get_numbers():
        nums.append(n)
    
    for n in filterfalse(lambda x: x % 2 != 0, nums):
        yield n

for n in filter_pairs():
    print(f"Valor: {n}")