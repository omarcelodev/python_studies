def potencia(exp):
    def calcular(x):
        return x ** exp
    
    return calcular

print(potencia(2)(5))
print(potencia(3)(2))