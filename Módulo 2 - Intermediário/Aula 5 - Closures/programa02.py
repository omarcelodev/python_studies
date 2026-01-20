#Exemplo de Closure que faz "Clicar"

#Criando multiplicadores diinâmicos

def multiplicador(n):
    def calcular(x):
        return x * n
    return calcular

dobro = multiplicador(2)
triplo = multiplicador(3)

print(dobro(10))
print(triplo(10))

#n ficou preso dentro da função