class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        return f"Olá, meu nome é {self.nome}"
    
    def aniversario(self):
        self.idade += 1

pessoa_1 = Pessoa("Marcelo", 20)
pessoa_2 = Pessoa("Ana Luisa", 19)

print(pessoa_1.falar())
print(f"Idade de {pessoa_1.nome}: {pessoa_1.idade}")

pessoa_1.aniversario()
print("Acabei de fazer aniversário")

print(f"Idade de {pessoa_1.nome}: {pessoa_1.idade}")


print("-" * 20)


print(pessoa_2.falar())
print(f"Idade de {pessoa_2.nome}: {pessoa_2.idade}")

pessoa_2.aniversario()
print("Acabei de fazer aniversário")

print(f"Idade de {pessoa_2.nome}: {pessoa_2.idade}")