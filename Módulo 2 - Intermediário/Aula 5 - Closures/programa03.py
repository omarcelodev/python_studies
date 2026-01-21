#Closure com estado mutável

def contador():
    total = 0 

    def incrementador():
        nonlocal total
        total += 1
        return total
    
    return incrementador

cont = contador()

print(cont())
print(cont())
print(cont())