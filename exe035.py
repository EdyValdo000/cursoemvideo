number1 = int(input('\033[1;30mDigite o 1º segmento: '))
number2 = int(input('\033[1;33mDigite o 2º segmento: '))
number3 = int(input('\033[1;31mDigite o 3º segmento: '))

if (number1 + number2 > number3) and (number1 + number3 > number2) and (number3 + number2 > number1) :
    print('\033[1;32mConsegues formar um triângulo com esses segmentos\033[m')
else:
    print('\033[1;30;41mNão da para formar um triângulo com esses valores, tenta de novo\033[m')
