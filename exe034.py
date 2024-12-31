salario = float(input('\033[33;1mQual é o teu salário?\n'))
salarioRef = 1250.00

if salario <= salarioRef:
    print('O seu novo salário é \033[1;32m{}\033[m\033[33;1mKz\033[m'.format(salario+(salario*0.15)))
else:
    print('O seu novo salário é \033[1;32m{}\033[m\033[33;1mKz\033[m'.format(salario+(salario*0.1)))