# Herança
# -Armadilha comum

# -Exemplo clássico:

class Animal:
    def fazer_som(self):
        pass
# -> Ok, funciona


# Onde a galera se perde

class Animal:
    def comer(self):
        print("Comendo...")

    def dormir(self):
        print("Dormindo...")

    def voar(self):
        print("Voando")
    
# -Ai você cria

class Cachorro(Animal):
    pass
class Peixe(Animal):
    pass

# -Peixe Voando
# -Cachorro respirando de baixo d'agua