from random import randint
from time import sleep
number = int(input('Digite um número de 0 até 5: '))
print('Processando...')
sleep(2)
sorte = randint(0,5)
if number == sorte:
    print('Acertaste o número sorteado')
else:
    print('Tenta de novo mais tarde!')