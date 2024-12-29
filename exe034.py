salario = float(input('Qual é o teu salário?\n'))
salarioRef = 1250.00

if salario <= salarioRef:
    print('O seu novo salário é {}Kz'.format(salario+(salario*0.15)))
else:
    print('O seu novo salário é {}Kz'.format(salario+(salario*0.1)))