number = int(input('Digite um número inteiro: '))
antecessor = number - 1
sucessor = number + 1
print('O antecessor de \033[34m{}\033[m é \033[31m{}\033[m'.format(number,antecessor), end =' ')
print('e o sucesor de \033[34m{}\033[m é \033[33m{}\033[m'.format(number,sucessor))