from datetime import date
ano= date.today().year
pessoa = dict()

pessoa ['Nome'] = str(input('Nome: '))
data = int(input('Ano de nascimento: '))
pessoa['Idade'] = abs(data - ano)

pessoa['Ctps'] = int(input('Carteira de trabalho: '))
if pessoa['Ctps'] != 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Seu salário: '))
    pessoa['Aposentadoria'] = abs(pessoa['Contratação'] - data) + 35

for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')