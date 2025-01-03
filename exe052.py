num = int(input('Digite um número: '))
teste = True
for e in range(num,0,-1):
    if num % e == 0 and num != e != 1:
        teste = False
    if num % e == 0:
        print('\033[33;1m{}\033[m'.format(e),end=' ')
    else:
        print('\033[31;1m{}\033[m'.format(e),end=' ')        
if teste:
    print('\033[36;1m\nO número é primo\033[m')
else:
    print('\033[31;1m\nO número não é primo\033[m')