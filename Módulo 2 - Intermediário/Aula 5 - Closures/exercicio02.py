def contador():
    total = 0

    def incrementador():
        nonlocal total
        total += 2
        return total
    return incrementador

cont = contador()

print(cont())
print(cont())
print(cont())
print(cont())