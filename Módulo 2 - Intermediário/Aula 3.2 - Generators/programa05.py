#Generator com yield

def contar_ate(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# Isso não retorna uma lista
# Ele "pausa" mp yield

# Uso
for num in contar_ate(5):
    print(num)