name = input('Qual é o seu nome? ')
busca = 'Coelho'
print('Se o teu nome tem Coelho')
print('\033[1;31m',busca in name.strip().title(),end='\033[m')