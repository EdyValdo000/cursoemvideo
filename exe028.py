from random import randint
number = int(input('Digite um número de 0 até 5: '))
sorte = randint(0,5)
if number == sorte:
    print('Acertaste o número sorteado')
else:
    print('Tenta de novo mais tarde!')