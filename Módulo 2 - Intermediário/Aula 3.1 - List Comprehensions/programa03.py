# List Comprehesions com condição

pares = [n for n in range(10) if n % 2 == 0]
print(pares)

# Isso substitui o seguinte código:
for n in range(10):
    if n % 2 == 0:
        pares.append(n)
print(pares)   