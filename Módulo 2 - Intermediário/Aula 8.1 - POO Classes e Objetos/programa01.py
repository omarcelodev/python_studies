# Criando uma classe

# -Em python, classe começa com class e nome em maiúsculo

class Pessoa: #Definição do molde

    def falar(self): # Método (o que o objeto faz)
        print("Olá") # "self" = o proprio objeto está chamando o método

# Criando Objetos -> criando pessoas reais a partir desse molde

joao = Pessoa()
maria = Pessoa()

# -Ambos objetos são do tipo pessoa

# Atributos

joao.nome = "João"
joao.idade = 25

maria.nome = "Maria"
maria.idade = 22

# - Cada objeto tem seus próprios dados, mesmo sendo da mesma classe

print(joao.nome)
print(maria.nome)

# Vamos utilizar o método que criamos (def falar)

joao.falar()
maria.falar()