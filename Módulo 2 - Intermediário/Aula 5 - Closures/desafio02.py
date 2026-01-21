def acumulador():
    total = 0

    def soma(x):
        nonlocal total
        total += x

        return total
    return soma

soma = acumulador()

print(soma(1))
print(soma(1))
print(soma(1))
print(soma(1))
print(soma(1))