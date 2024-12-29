import emoji
# emoji.emojize('Olá mundo :globe_showing_Europe-Africa:')
velocidade = float(input('Qual é a velocidade do veículo? '))
multaRef = 7
limVelocidade = 80.0

if velocidade == limVelocidade:
    print('Estás no lim, reduz a velocidade')
if velocidade > limVelocidade:
    print('O teu carro ultrapassou o lim de velocidade e a multá é de {}kz'.format((velocidade-limVelocidade)*multaRef))
else:
    print('Estás dentro do lim de velocidade.')