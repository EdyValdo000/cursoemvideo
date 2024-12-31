p1 = float(input('Qual é a nota da p1? '))
p2 = float(input('Qual é a nota da p2? '))
med = (p1 + p2) / 2
print('A media entre a p1=\033[1;36m{:.1f}\033[m e a p2=\033[1;36m{:.1f}\033[m é \033[1;33m{:.1f}\033[m'.format(p1,p2,med))