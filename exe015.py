day = int(input('Quantos dias o carro foi alugado? '))
distance = float(input('Qual é a distância percorrida pelo veículo em Km? '))
"60Kz por dia"
"0.15Kz por Km percorrido"

moneyDay = 60 * day
print('O total a se pagar por dia é {:.2f}Kz'.format(moneyDay))

moneyDistance = 0.15 * distance
print('O total a se pagar por Km percorrido é {:.2f}Kz'.format(moneyDistance))

moneyTotal = moneyDay + moneyDistance
print('O valor a se pagar pelo alugel do veículo é {:.2f}Kz'.format(moneyTotal))