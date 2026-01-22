"""
    Encapsulamento

    -Esconder o que não deve ser mexido diretamente e controlar como os dados são acessados
    -Nem tudo pode ficar escancarado, o objeto se protege de uso errado, evita bug

    Exemplos: pessoa.idade = -300 
              pessoa.nome = ""
    
    Isso quebra: lógica, regra de négocio
"""

"""
    Encapsulamento em python
    
    -Python não tem private de verdade como o java mas tem convenção forte

    _atributo -> nao mexa nisso diretamente
    __atributo -> name mangling(mais protegido ainda)
"""

#Exemplo prático

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo # -> Protegido

#Jeito errado

conta = ContaBancaria()
conta.saldo = -1000 # GAMBIARRA
        
