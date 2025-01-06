sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('\033[mDigite o seu sexo \033[36;1mM\033[m ou \033[35;1mF\033[m: ')).upper()[0]
    if sexo not in 'MF':
        print('\033[31;1mDigitaset mal, tente de novo')
    else:
        if sexo == 'M':
            print('\033[32;1mdigitaste bem\033[m, o seu sexo é \033[36;1m{}\033[m'.format(sexo))
        else:
            print('\033[32;1mdigitaste bem\033[m, o seu sexo é \033[35;1m{}\033[m'.format(sexo))