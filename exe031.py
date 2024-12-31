distance = float(input('\033[1;36mDigite a distancia da sua viagem: \033[m'))
distanceRef = 200.0
moneyRef1 = 0.5
moneyRef2 = 0.45
if distance <= distanceRef:
    print('O valor que vais pagar pela viagem é de \033[1;32m{}Kz\033[m'.format(distance*moneyRef1))
else:
    print('O valor que vais pagar pela viagem é de \033[1;32m{}Kz\033[m'.format(distance*moneyRef2))