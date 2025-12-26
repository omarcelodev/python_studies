#Exercicios de *args

def media(*args):
    soma = sum(args) 
    numeros = args
    
    media = soma / numeros

    return media

print(media(1, 2, 3, 4, 5, 6))