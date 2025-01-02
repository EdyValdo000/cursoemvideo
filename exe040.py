p1 = float(input('Nota da p1: '))
p2 = float(input('Nota da p2: '))
med = (p1+p2)/2

if p1 < 5.0:
    P1 = '\033[1;31m{}\033[m'.format(p1)
elif p1 == 5.0:
    P1 = '\033[1;33m{}\033[m'.format(p1)
else:
    P1 = '\033[1;32m{}\033[m'.format(p1)

if p2 < 5.0:
    P2 = '\033[1;31m{}\033[m'.format(p2)
elif p2 == 5.0:
    P2 = '\033[1;33m{}\033[m'.format(p2)
else:
    P2 = '\033[1;32m{}\033[m'.format(p2)    

if med<5.0:
    print('P1: {} P2: {}'.format(P1,P2))
    print('Média: \033[1;31m{:.1f}\033[m'.format(med))
    print('\033[1;31mREPROVADO\033[m')
elif 5 <= med and med <6.9:
    print('P1: {} P2: {}'.format(P1,P2))
    print('Média: \033[1;33m{:.1f}\033[m'.format(med))
    print('\033[1;33mRECUPERAÇÂO\033[m')
elif med > 7.0:
    print('P1: {} P2: {}'.format(P1,P2))
    print('Média: \033[1;32m{:.1f}\033[m'.format(med))
    print('\033[1;32mAPROVADO\033[m')
