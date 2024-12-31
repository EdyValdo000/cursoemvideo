number = int(input('Digite um número inteiro: '))
double = number * 2
trip = number * 3
quot = pow(number,1/2)

print('O dobro de \033[1;30;41m{}\033[m é \033[31m{}\033[m'.format(number,double))
print('O triplo de \033[1;30;41m{}\033[m é \033[32m{}\033[m'.format(number,trip))
print('A raiz quadrada de \033[1;30;41m{}\033[m é \033[33m{}\033[m'.format(number,quot))