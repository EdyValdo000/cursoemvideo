p1 = float(input('Nota da p1: '))
p2 = float(input('Nota da p2: '))
med = (p1+p2)/2
if med<5.0:
    print('Média: \033[1;31m{:.2f}\033[m'.format(med))
    print('\033[1;31mREPROVADO\033[m')
elif 5 <= med and med <6.9:
    print('Média: \033[1;33m{:.2f}\033[m'.format(med))
    print('\033[1;33mRECUPERAÇÂO\033[m')
elif med > 7.0:
    print('Média: \033[1;32m{:.2f}\033[m'.format(med))
    print('\033[1;32mAPROVADO\033[m')