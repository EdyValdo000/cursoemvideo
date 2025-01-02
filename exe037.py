number = int(input('Digite um número inteiro: '))
mode = int(input("""Queres converter o número para que base?\033[1;33m\n1-->binario\033[m\033[1;32m\n2-->octal\033[m\033[1;36m\n3-->hexadecimal\033[m\n"""))
if mode == 1:
    print('O número em binário é \033[1;33m{}\033[m'.format(bin(number).replace('0b','')))
elif mode == 2:
    print('O número em octal é \033[1;32m{}\033[m'.format(oct(number).replace('0o','')))
elif mode == 3:
    print('O número em hexadecimal é \033[1;36m{}\033[m'.format(hex(number).replace('0x','')))
else:
    print('\033[1;31mO modo está incorecto\033[m')