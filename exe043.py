peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura em metros: '))
IMC = peso / altura**2
print('O IMC dessa pessoa é de',end=' ')

if IMC < 18.5:
    print('\033[31;1m{:.1f}\033[m Kg/m^2'.format(IMC))
    print('\033[31;1mEstás a baixo do peso\033[m')
elif 18.5 <= IMC < 25:
    print('\033[32;1m{:.1f}\033[m Kg/m^2'.format(IMC))
    print('\033[32;1mEstás no peso ideal\033[m')
elif 25 <= IMC <= 30:
    print('\033[33;1m{:.1f}\033[m Kg/m^2'.format(IMC))
    print('\033[33;1mSobrepeso\033[m')
elif 30 < IMC <= 40:
    print('\033[35;1m{:.1f}\033[m Kg/m^2'.format(IMC))
    print('\033[35;1mObesidade\033[m')
else:
    print('\033[1;42m{:.1f}\033[m Kg/m^2'.format(IMC))
    print('\033[1;42;1mObesidade mobida!!!\033[m')