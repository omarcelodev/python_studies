# Closures

# -É quando uma função "lembra" de variáveis do escopo onde ela foi criada, mesmo depois desse escopo
# ter acabado

# Exemplos Simples

def externa():
    x = 10

    def interna():
        return x

    return interna

func = externa()
print(func())