number1 = int(input('Digite o 1º segmento: '))
number2 = int(input('Digite o 2º segmento: '))
number3 = int(input('Digite o 3º segmento: '))

if (number1 + number2 > number3) and (number1 + number3 > number2) and (number3 + number2 > number1) :
    print('Consegues formar um triângulo com esses segmentos')
else:
    print('Não da para formar um triângulo com esses valores, tenta de novo')
