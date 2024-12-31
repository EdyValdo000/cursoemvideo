from math import trunc
number = float(input('Digite um número real: '))
print('A parte interia de {} é \033[1;36m{}\033[m'.format(number,trunc(number)))