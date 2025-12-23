# O que é um generator?
# Generator é uma função que produz valores aos poucos, sob demanda, em vez de criar tudo de uma vez
# na memória

# Lista
lista = [x * 2 for x in range(1_000_000)] # -> Cria 1 milhão de itens na RAM

#Generator
gen = (x * 2 for x in range(1_000_000)) # --> Cria 0 itens, só gera quando alguem pede