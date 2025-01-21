from time import sleep
from random import randint
from operator import itemgetter
contador = 1

pessoas = {
    'jogador1' : randint(1,6),
    'jogador2' : randint(1,6),
    'jogador3' : randint(1,6),
    'jogador4' : randint(1,6),
}

for k, v in pessoas.items():
    print(f'O {k} tirou {v}')
    
print('\nRanking dos jogadores\n')

oragnizado = dict(sorted(pessoas.items(),  key=itemgetter(1), reverse=True))
for k, v in oragnizado.items():
    print(f'O {contador}º lugar foi {k} e teve {v}')
    contador += 1