def maior_que(x):
    def validar(y):
        return y > x
       
    return validar

valida = maior_que(10)

print(valida(5))
print(valida(15))

