valor = input('Digite um algo: ')
print('\n O que digitaste é')
print('O valor é do tipo: {}'.format(type(valor)))
print('É composto apenas de números: {}'.format(valor.isnumeric()))
print('É composto apenas de letras: {}'.format(valor.isalpha()))
print('É composto por letras e números: {}'.format(valor.isalnum()))
print('É composto só por letras maiusculas: {}'.format(valor.isupper()))
print('É composto só por letras minusculas: {}'.format(valor.islower()))
print('O valor é apenas espaço: {}\n'.format(valor.isspace()))
