#Exercicios de *args
def ex1():
    def media(*args):
        soma = sum(args) 
    
        media = soma / len(args)

        return media

    print(media(1, 2, 3, 4, 5, 6))

def ex2():
    def argumentos(*args):
        for i in args:
            print(i)
       
    argumentos(1, 2, 3, 4, 5, 6)

ex2()