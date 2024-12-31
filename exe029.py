import emoji
# emoji.emojize('Olá mundo :globe_showing_Europe-Africa:')
velocidade = float(input('Qual é a velocidade do veículo? '))
multaRef = 7
limVelocidade = 80.0

if velocidade > limVelocidade:
    print('\033[1;30;41mO teu carro ultrapassou o lim de velocidade e a multá é de\033[m \033[1;31m{}kz\033[m'.format((velocidade-limVelocidade)*multaRef))
if velocidade == limVelocidade:
    print('\033[1;32mEstás no lim, reduz a velocidade\033[m')
if velocidade < limVelocidade:
    print('\033[1;36mEstás dentro do lim de velocidade.\033[m')