def function(**kwargs):
    for chave in kwargs.items():
        if chave == "nome":
            print("A chave 'nome' existe")
            break
        else:
            print("Erro")
            break

function(idade = 20, curso = "Engenharia de Software")