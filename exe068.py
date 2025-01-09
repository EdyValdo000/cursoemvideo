#O meu par ou impar é melhor que o par ou impar tradicional
#Eu compliquei mais, só o jogador é que diz par ou impar, o pc só sorteia um número
import emoji
from random import randint
from time import sleep
resultado = ''
numHumano = numPc = victórias = 0
while True:
    print('='*50)
    print('Vamos jogar par ou impar\n')
    numHumano = int(input('Digite um valor: \033[1;36m'))
    jogadaHumano = str(input('Par ou Impar? [P/I]: ')).upper().strip()[0]
    if jogadaHumano == 'P':
        jogadaHumano = 'PAR'
    else:
        jogadaHumano = 'IMPAR'
            
    numPc = randint(0,5)    
    if randint(2,3) == 2:
        jogadaPc = 'PAR'
    else:
        jogadaPc = 'IMPAR'

    print(emoji.emojize('\n:robot: \033[35;1mPROCESSANDO...'))
    sleep(2)

    total = numHumano + numPc
    if total % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    
    print(f'Tu jogaste {numHumano} e disseste {jogadaHumano}, e eu jogeui {numPc} e disse {jogadaPc}...\033[m\n')

    if jogadaHumano == resultado and jogadaPc != resultado:
        victórias += 1
        print(f'Tu escolheste {jogadaHumano} e o pc escolheu {jogadaPc} e o número {total} é {resultado}')
        print(emoji.emojize(f'\033[1;33mVenceste\033[m, :robot:\033[1;35m eu não vou desistir...\033[m'))        
    
    elif jogadaHumano != resultado and jogadaPc == resultado:
    
        print(emoji.emojize('\033[1;31mPerdeste\033[m, :robot:\033[1;35m eu ganhei...\033[m'))
        if victórias == 0:
            print(f'\033[35;1mE tu não ganhaste nem uma vez.\033[m')            
        elif victórias == 1:
            print(f'Mas tu conseguiste \033[33;1m{victórias}\033[m victória')
        else:
            print(f'Mas tu conseguiste \033[33;1m{victórias}\033[m victórias consecutivas')            
        break
    
    elif jogadaHumano == resultado and jogadaPc == resultado:
        print(f'Deu empate, os dois escolheram {jogadaHumano}, e o {total} é {resultado}')
    
    else:
        print(emoji.emojize(f':robot: \033[1;35mOs dois escolhemos a opção errada kkkk\033[m o número {total} é {resultado}'))