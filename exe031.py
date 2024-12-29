distance = float(input('Digite a distancia da sua viagem: '))
distanceRef = 200.0
moneyRef1 = 0.5
moneyRef2 = 0.45
if distance <= distanceRef:
    print('O valor que vais pagar pela viagem é de {}Kz'.format(distance*moneyRef1))
else:
    print('O valor que vais pagar pela viagem é de {}Kz'.format(distance*moneyRef2))