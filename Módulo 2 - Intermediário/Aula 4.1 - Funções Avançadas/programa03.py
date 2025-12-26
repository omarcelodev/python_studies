# filter() - seleção de dados
# filtra e elementos de um iterável, aplica uma função e critério que retorna True ou False 
# e retorna um iterador contendo apenas os itens para os quais a função retornou True

#Estruturaa
# filter(condição, iterável)

#Exemplo

nums = [1, 2, 3, 4]
pares = filter(lambda x: x % 2 == 0, nums)