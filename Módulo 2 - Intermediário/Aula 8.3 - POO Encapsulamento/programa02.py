# Jeito certo: métodos controlando acesso

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
    
    def ver_saldo(self):
        return self._saldo
    
# Agora ninguem coloca saldo negativo, regra fica centralizada, cóigo mais seguro
