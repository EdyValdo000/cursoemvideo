from random import randint
from time import sleep
jogador = int(input("""Escolhe a tua jogada:
0--> \033[1;31mpedra\033[m
1--> \033[1;30mpapel\033[m
2--> \033[1;34mtesoura\033[m
"""))

pc = randint(0,2)
print('\033[35;1mPROCESSANDO....\033[m')
sleep(1)

escolhas = ['pedra', 'papel', 'tesoura']

if jogador == 0:
    print('Tu jogaste \033[1;31m{}\033[m e o computador jogou \033[1;35m{}\033[m'.format(escolhas[jogador],escolhas[pc]))
elif jogador == 1:
    print('Tu jogaste \033[1;30m{}\033[m e o computador jogou \033[1;35m{}\033[m'.format(escolhas[jogador],escolhas[pc]))
elif jogador == 2:
    print('Tu jogaste \033[1;34m{}\033[m e o computador jogou \033[1;35m{}\033[m'.format(escolhas[jogador],escolhas[pc]))

if escolhas[pc] == escolhas[jogador]:
    print('\033[33;1mDeu empate\033[m')
else:
    if escolhas[pc] == 'pedra' and escolhas[jogador] == 'tesoura':
        print('\033[1;31mPerdeste, tenta de novo kkkk\033[m')
    elif escolhas[pc] == 'pedra' and escolhas[jogador] == 'papel':
        print('\033[1;32mGANHASTE\033[m')

    elif escolhas[pc] == 'papel' and escolhas[jogador] == 'pedra':
        print('\033[1;31mPerdeste, tenta de novo kkkk\033[m')
    elif escolhas[pc] == 'papel' and escolhas[jogador] == 'tesoura':
        print('\033[1;32mGANHASTE\033[m')

    elif escolhas[pc] == 'tesoura' and escolhas[jogador] == 'papel':
        print('\033[1;31mPerdeste, tenta de novo kkkk\033[m')
    elif escolhas[pc] == 'tesoura' and escolhas[jogador] == 'pedra':
        print('\033[1;32mGANHASTE\033[m')
print('\n')  