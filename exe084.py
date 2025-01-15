pessoas = list()
dados = []
Nomes = list()
Pesos = list()
resposta = "S"
nome = ''
peso = númeroDePessoas = maisLeve = maisPesada = 0
while True:
    nome = str(input('Digite o nome: '))
    peso = float(input('Digite o peso: '))    
    dados.append(nome)
    dados.append(peso)
    
    Nomes.append(nome)
    Pesos.append(peso)
    pessoas.append(dados[:])
    númeroDePessoas += 1
    dados.clear()

    while True:
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SsNn':
            break
        else:
            print('Erro. ', end='')

    if resposta in 'Nn':
        break

maisLeve = min(Pesos)
maisPesada = max(Pesos)

if númeroDePessoas == 1 and pessoas[0][0][-1] in 'Aa':
    print(f'Foi registada {númeroDePessoas} pessoa')
elif númeroDePessoas == 1 and pessoas[0][0][-1] in 'OoIiUuEe':
    print(f'Foi registado {númeroDePessoas} pessoa')
elif númeroDePessoas == 1:
    print(f'Foi registada {númeroDePessoas} pessoa')
else:
    print(f'Foram registados {númeroDePessoas} pessoas')

if Pesos.count(maisLeve) == 1 and pessoas[0][0][-1] in 'Aa':
    print('A pessoa mais leve pesa ',end='')
    for i, e in enumerate(Pesos):
        if maisLeve == e:
            print(f'{Pesos[i]}Kg e é a {Nomes[i]}')    
elif Pesos.count(maisLeve) == 1 and pessoas[0][0][-1] in 'OoIiUuEe':
    print('A pessoa mais leve pesa ',end='')
    for i, e in enumerate(Pesos):
        if maisLeve == e:
            print(f'{Pesos[i]}Kg e é o {Nomes[i]}')  
elif Pesos.count(maisLeve) == 1:
    print('A pessoa mais leve pesa ',end='')
    for i, e in enumerate(Pesos):
        if maisLeve == e:
            print(f'{Pesos[i]}Kg e é a {Nomes[i]}') 
else:
    print(f'As pessoas mais leves pesam {maisLeve}Kg ',end='')
    for i, e in enumerate(Pesos):
        if maisLeve == e:
            print(f"{pessoas[i][0]}",end=' ')
    print('')


if Pesos.count(maisPesada) == 1 and pessoas[0][0][-1] in 'Aa':
    print('A pessoa mais pesada pesa ',end='')
    for i, e in enumerate(Pesos):
        if maisPesada == e:
            print(f'{Pesos[i]}Kg e é o {Nomes[i]}')  
elif Pesos.count(maisPesada) == 1 and pessoas[0][0][-1] in 'OoIiUuEe':
    print('A pessoa mais pesada pesa ',end='')
    for i, e in enumerate(Pesos):
        if maisPesada == e:
            print(f'{Pesos[i]}Kg e é o {Nomes[i]}')  
elif Pesos.count(maisPesada) == 1:
    print('A pessoa mais pesada pesa ',end='')
    for i, e in enumerate(Pesos):
        if maisPesada == e:
            print(f'{Pesos[i]}Kg e é a {Nomes[i]}')    
else:
    print(f'As pessoas mais pesadas pesam {maisPesada}Kg ',end='')
    for i, e in enumerate(Pesos):
        if maisPesada == e:
            print(f"{pessoas[i][0]}",end=' ')