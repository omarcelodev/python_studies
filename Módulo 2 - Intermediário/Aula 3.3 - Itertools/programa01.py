# O que é itertools?
# Itertools é um módulo quue fornece generators

#Os 4 mais importantes 

#count() - Contador infinito
def count():
    from itertools import count

    for n in count(1):
        print(n)
        if n == 5:
            break

#cycle() - loop infinito
def cycle():
    from itertools import cycle

    for x in cycle(["A", "B", "C"]):
        print(x)

#islice() - fatiar generator
def islice():
    from itertools import islice
    from itertools import count

    nums = count(1)

    for n in islice(nums, 5):
        print(n)

#chain() - encadear iteráveis
def chain():
    from itertools import chain

    for n in chain([1,2], [3,4], [5], [10], [1322]):
        print(n)

chain()