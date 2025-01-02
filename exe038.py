firstNumber = int(input('Digite o 1º número: '))
secondNumber = int(input('Digite o 2º número: '))
if firstNumber > secondNumber:
    print('O 1º número (\033[36m{}\033[m) é maior'.format(firstNumber))
elif secondNumber > firstNumber:
    print('O 2º número (\033[1;36m{}\033[m) é o maior.'.format(secondNumber))
else:
    print('\033[1;32mOs dois números são iguais\033[m')
