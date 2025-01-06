termo = int(input('1º termo da PA: '))
razão = int(input('Razão da PA: '))
valor = 10
contador = 0
while valor != 0:
    limTermo = termo + (valor - 1)*razão
    while termo <= limTermo:
        print('\033[33;1m',termo,end=';')
        termo += razão
        contador += 1
    if razão < 0:
        while termo >= limTermo:
            print('\033[33;1m',termo,end=';')
            termo += razão
            contador += 1
    print('\033[m PAUSADO...')
    valor = int(input('Queres ver mais quantos termos? '))
print('\033[1;36mO prográma terminou e mostrou \033[1;33m{}\033[1;36m termos da PA\033[m'.format(contador))
print('\033[1;36mFIM\033[m') 