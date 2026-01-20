def externa():
    total = 0

    def interna(x):
        nonlocal total
        total += x

        return total
    return interna

soma = externa()

print(soma(1))
print(soma(1))
print(soma(1))
print(soma(1))
print(soma(1))