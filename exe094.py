# [ {nome: xxx, idade: 12, sexo: M}, {nome: xxx, idade: 12, sexo: M}, {nome: xxx, idade: 12, sexo: M}]
pessoas = list()
dados = {}
listMulheres = []
listPessoasComIdadeAcimaDaMédia = []
resposta = 'S'
totalPessoas = totalIdades = 0

while True:
    dados['Nome'] = str(input('Nome: ')).strip()
    
    dados['Idade'] = int(input('Idade: '))
    totalIdades += dados['Idade']
    
    while True:
        dados['Sexo'] = str(input('Qual é o sexo? [M/F] ')).strip()[0]
        if dados['Sexo'] in 'MmFf':
            break
    
    if dados['Sexo'] in 'Ff':
        listMulheres.append(dados['Nome'])

    pessoas.append(dados.copy())
    totalPessoas += 1
    
    dados.clear()
    
    while True:
        resposta = str(input('Queres contiinuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SsNn':
            break
        else:
            print('Erro ',end='')
    
    if resposta in 'Nn':
        break

média = totalIdades/totalPessoas

print(f'\nForam registadas {totalPessoas} pessoas')
print(f'A média de idades é {média:.2f} anos')
print(f'A lista das mulheres é {listMulheres}')
print(f'Pessoas com idades maior que a média:')
for c in range(0, len(pessoas)):
   if pessoas[c]['Idade'] > média:
       print(f'=» O {pessoas[c]['Nome']} com {pessoas[c]['Idade']} anos')