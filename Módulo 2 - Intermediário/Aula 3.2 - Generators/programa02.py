# Generator expression

# Já estudamos isso
lista = [x ** 2 for x in range(5)]

# Generator é a mesma coisa, só troca [] por ()
gen = (x ** 2 for x in range(5))
print(gen) # Não vai imprimir nada pq ele ainda nao execeutou. 

# Para usar
for n in gen:
    print(n)