address = input('Qual é a tua morada: ')
print('Se a tua morada começa com Rangel\033[1;30;41m')
print('Rangel' in address.strip().title().split()[0], end='\033[m')
