fullName = input('Digite o seu nome: ')
firstName = fullName.split()[0]
lastName = fullName.split()[-1]
print('O seu primeiro nome é \033[4;36m{}\033[m'.format(firstName))
print('O seu último nome é \033[4;36m{}\033[m'.format(lastName))