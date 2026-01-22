class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    def ver_preco(self):
        return self._preco

    def alterar_preco(self, valor):
        if valor > 0:
            self._preco = valor
            return True
        return False
    

cafe = Produto("Café", 35.90)
arroz = Produto("Arroz", 44.90)
oleo = Produto("Óleo", 9.90)

print(f"{cafe.nome}: R$ {cafe.ver_preco():.2f}")
print(f"{arroz.nome}: R$ {arroz.ver_preco():.2f}")
print(f"{oleo.nome}: R$ {oleo.ver_preco():.2f}")

#Iremos alterar o preco do oleo e do cafe 

#Jeito certo
print("\n===OLEO===")
valor = float(input("Digite o valor: R$ "))

if not oleo.alterar_preco(valor):
    print("Preço Inválido")

print(f"{oleo.nome}: R$ {oleo.ver_preco():.2f}")

#Jeito errado
print("\n===CAFE===")
valor = float(input("Digite o valor: R$ "))

if not cafe.alterar_preco(valor):
    print("Preço Inválido")

print(f"{cafe.nome}: R$ {cafe.ver_preco():.2f}")


