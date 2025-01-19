aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
print(f'Nome é igual a {aluno['Nome']}')
print(f'Média é igual a {aluno['Média']}')
if aluno['Média'] >= 10 and aluno['Nome'][-1] in 'AaUu':
    print(f'A situação é igual a Aprovada')
elif aluno['Média'] >= 10 and aluno['Nome'][-1] in 'OoIiYy':
    print(f'A situação é igual a Aprovado')
elif aluno['Média'] < 10 and aluno['Nome'][-1] in 'AaUu':
    print(f'A situação é igual a Reprovada')
else:
    print(f'A situação é igual a Reprovado')