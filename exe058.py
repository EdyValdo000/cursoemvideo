from random import randint
from time import sleep
import emoji
pc = randint(1,10)
print(emoji.emojize(':robot: \033[35;1mPROCESSANDO...\033[m'))
sleep(2)
print(emoji.emojize(':robot: \033[35;1mPensei em um número entre [1;10], consegues adivinhar?\033[m'))
tentativas = palpite = 0
while palpite != pc:
    palpite = int(input('\nDigite o número que o pc pensou: '))
    if palpite != pc:
        tentativas += 1
        print('\033[1;31mEraste, tenta de novo ',end='')
        if palpite > pc:
            print('o número é menor\033[m')
        elif tentativas < pc:
            print('o número é maior\033[m')
if tentativas == 0:
    print('\033[1;36mTu és muito sortudo, de 1ª!\033[m')
else:
    print('\033[1;33mConsegiste acertar,\033[m com {} tentativas.'.format(tentativas))