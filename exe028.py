from random import randint
from time import sleep
number = int(input('Digite um número de 0 até 5: '))
print('\033[1;36mProcessando...\033[m')
sleep(2)
sorte = randint(0,5)
if number == sorte:
    print('\033[1;32;40mAcertaste o número sorteado\033[m')
else:
    print('\033[1;31mTenta de novo mais tarde!\033[m')