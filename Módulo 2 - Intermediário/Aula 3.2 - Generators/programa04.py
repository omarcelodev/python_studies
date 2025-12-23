#Generator morre depois de percorrido:

gen = (x for x in range(3))

for x in gen:
    print(x)

for x in gen:
    print(x) #Não imprime nada