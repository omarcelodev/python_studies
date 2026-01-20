def maior_que(x):
    def validar(y):
        if y > x:
            return True
        else:
            return False
        
    return validar

valida = maior_que(10)

print(valida(5))
print(valida(15))

