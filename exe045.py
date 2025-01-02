from random import randint, shuffle
from time import sleep 
import emoji
escolhasEmoji = [
    f"\033[1;31mPedra\033[m {emoji.emojize(':raised_fist:')}",
    f"\033[1;30mPapel\033[m {emoji.emojize(':hand_with_fingers_splayed:')}",
    f"\033[1;34mTesoura\033[m {emoji.emojize(':victory_hand:')}",
]
print("""Escolhe a tua jogada:
0--> {}
1--> {}
2--> {}""".format(escolhasEmoji[0],escolhasEmoji[1],escolhasEmoji[2]))

jogador = int(input('Digite a sua jogada: '))

pc = randint(0,2)
print(emoji.emojize('\n:robot: \033[35;1mPROCESSANDO...'))
sleep(1)
print(escolhasEmoji[0])
sleep(1)
print(escolhasEmoji[1])
sleep(1)
print(escolhasEmoji[2],'\n')
sleep(1)

escolhas = ['pedra', 'papel', 'tesoura']

if jogador == 0:
    print('Tu jogaste \033[1;31m{}\033[m e o computador jogou \033[1;35m{}\033[m'.format(escolhas[jogador],escolhas[pc]))
elif jogador == 1:
    print('Tu jogaste \033[1;30m{}\033[m e o computador jogou \033[1;35m{}\033[m'.format(escolhas[jogador],escolhas[pc]))
elif jogador == 2:
    print('Tu jogaste \033[1;34m{}\033[m e o computador jogou \033[1;35m{}\033[m'.format(escolhas[jogador],escolhas[pc]))

if escolhas[pc] == escolhas[jogador]:
    print(emoji.emojize('\033[33;1mDeu empate\033[m :sneezing_face:'))
else:
    if escolhas[pc] == 'pedra' and escolhas[jogador] == 'tesoura':
        print(emoji.emojize('\033[1;31mPerdeste, tenta de novo kkkk\033[m :unamused_face:'))
    elif escolhas[pc] == 'pedra' and escolhas[jogador] == 'papel':
        print(emoji.emojize('\033[1;32mGANHASTE\033[m :star-struck:'))

    elif escolhas[pc] == 'papel' and escolhas[jogador] == 'pedra':
        print(emoji.emojize('\033[1;31mPerdeste, tenta de novo kkkk\033[m :unamused_face:'))
    elif escolhas[pc] == 'papel' and escolhas[jogador] == 'tesoura':
        print(emoji.emojize('\033[1;32mGANHASTE\033[m :star-struck:'))

    elif escolhas[pc] == 'tesoura' and escolhas[jogador] == 'papel':
        print(emoji.emojize('\033[1;31mPerdeste, tenta de novo kkkk\033[m :unamused_face:'))
    elif escolhas[pc] == 'tesoura' and escolhas[jogador] == 'pedra':
        print(emoji.emojize('\033[1;32mGANHASTE\033[m :star-struck:'))
print('\n')