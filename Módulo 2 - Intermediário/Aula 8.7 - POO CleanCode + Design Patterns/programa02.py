# Design Patterns

# 1. Strategy
#   - Trocar comportamento sem mudar quem usa

chose = 0
pagamento = 0
class Pagamentos():
    def pagar(self, valor):
        pass

class Pix(Pagamentos):
    pass

class Cartao(Pagamentos):
    pass

class Boleto(Pagamentos):
    pass

# O sistema faz

pagamento.pagar(100)

# 2. Factory
#   -Hoje você faz:

if chose == 1:
    Pix()

#   -Ideia de Factory:

def pagamento_factory(chose):
    if chose == 1:
        return Pix()
    if chose == 2:
        return Cartao()
    
# Então o menu vira:

pagamento = pagamento_factory(chose)
print(pagamento.pagar(100))


# 3.Template Method
#   - Quando todas as classes seguem o mesmo fluxo: Validar, Calcular, Formatar. Mas mudam um pedaço