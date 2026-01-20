def operacoe(*args):
    soma = sum(args)
    maximo = max(args)
    minimo = min(args)

    print(f"soma: {soma}, max:{maximo}, min:{minimo}")

operacoe(1, 2, 3, 4, 5, 6)