day = int(input('\033[1;30;41mQuantos dias o carro foi alugado? '))
distance = float(input('Qual é a distância percorrida pelo veículo em Km? '))
"60Kz por dia"
"0.15Kz por Km percorrido"

moneyDay = 60 * day
print('\033[1;30;41mO total a se pagar por dia é\033[m \033[1;36m{:.2f}Kz\033[m'.format(moneyDay))

moneyDistance = 0.15 * distance
print('\033[1;30;41mO total a se pagar por Km percorrido é\033[m \033[1;36m{:.2f}Kz\033[m'.format(moneyDistance))

moneyTotal = moneyDay + moneyDistance
print('\033[1;30;41mO valor a se pagar pelo alugel do veículo é\033[m \033[1;36m{:.2f}Kz\033[m'.format(moneyTotal))