#List Comprehensions com transformação e filtro

quadrados_pares = [n ** 2 for n in range(10) if n % 2 == 0]
print(quadrados_pares)

"""
Regras de Ouro:
✔ Use list comprehension quando:
- a lógica cabe em **uma linha**
- é fácil de ler

❌ NÃO use quando:
- fica confuso
- tem muitos `if`
- lógica complexa

Legibilidade > elegância.
"""