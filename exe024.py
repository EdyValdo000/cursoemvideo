address = input('Qual é a tua morada: ')
print('Se a tua morada começa com Rangel')
print('Rangel' in address.strip().title().split()[0])