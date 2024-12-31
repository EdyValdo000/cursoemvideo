salarioBase = float(input('Qual é o teu salário actual? '))
aumento = salarioBase * 0.15
newSalario = salarioBase + aumento
print('O teu salário é \033[1;32m{:.2f}Kz\033[m e subiu para \033[1;32m{:.2f}Kz\033[m\n'.format(salarioBase,newSalario))