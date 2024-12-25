salarioBase = float(input('Qual é o teu salário actual? '))
aumento = salarioBase * 0.15
newSalario = salarioBase + aumento
print('O teu salário é {:.2f}Kz e subiu para {:.2f}Kz\n'.format(salarioBase,newSalario))