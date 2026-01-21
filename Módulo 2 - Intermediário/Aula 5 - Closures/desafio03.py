"""
def function():
    def execute(x):
        mensagem = x

        return mensagem
    
    return execute

mensagem = function()

print(mensagem("Executando Função..."))
"""

def executor(func):
    def executar():
        print("Executando função...")
        return func()
    
    return executar

def minha_funcao():
    return "Função executada!"

f = executor(minha_funcao)
print(f())