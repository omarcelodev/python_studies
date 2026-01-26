# Quando não usar POO?

# -> Scrit pquenos e automações simples

# -Exemplo:

valores = 0
total = sum(valores)
print(total)

# -Criar isso em POO seria um exagero desnecessário

class Soma:
    def calcular(self):
        pass

# -Regra: Se não existe estado + comportamento duradouro, não use POO 

# Use POO quando:
# -> O código vai crescer, tem regras de negócio, tem variação de comportamento