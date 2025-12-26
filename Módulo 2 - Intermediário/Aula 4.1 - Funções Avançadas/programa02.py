# Map() - Transformação de dados
#Aplica uma função a cada item de um iteravel e retorna um objeto map com os resultados

# Estrutura:
# map(função, iterável)

#Exemplo:
nums = [1, 2, 3]
resultado = map(lambda x: x * 2, nums)

for n in resultado:
    print(n)

#map não cria lista!
