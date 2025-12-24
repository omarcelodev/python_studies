# O itertools que conversa direto com oq fizemos

from itertools import filterfalse

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in filterfalse(lambda x: x % 2 != 0, nums):
    print(n)

#Quano usar itertools?

"""
Use quando:

- pipeline começar a ficar longo
- dados forem grandes
- quiser código mais expressivo

Não use quando:

- está aprendendo (como agora)
- clareza for mais importante que concisão
"""