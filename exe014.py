ºc = float(input('Digita a temperatura em ºC: '))
ºf = ºc * (9/5) + 32
print('\033[1;31m{:.1f}ºC\033[m equivale a \033[1;36m{:.1f}ºF\033[m'.format(ºc,ºf))