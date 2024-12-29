fullName = input('Digite o seu nome: ')
firstName = fullName.split()[0]
lastName = fullName.split()[-1]
print('O seu primeiro nome é {}'.format(firstName))
print('O seu último nome é {}'.format(lastName))