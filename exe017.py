from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = hypot(co,ca)
print('O valor da hipotenusa é \033[1;32m{}\033[m'.format(h))