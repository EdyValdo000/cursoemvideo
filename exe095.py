jogador = dict()
golos = list()
jogadores = list()
golosElementos = []
resposta = 'S'
modo = 0
while True:

    jogador ['Nome'] = str(input('Nome do jogador: '))
    partidas = totalGolos = 0
    partidas = int(input(f'Quantas partidas o {jogador["Nome"]} jogou: '))

    for c in range(1,partidas+1):
        golosElementos = int(input(f'No {c}º jogo marcou quantos golos? '))
        totalGolos += golosElementos
        golos.append(golosElementos)
    jogador['Golos'] = golos[:]
    jogador['Total'] = totalGolos

    jogadores.append(jogador.copy())
    totalGolos = 0
    golos.clear()
    jogador.clear()

    while True:        
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SsNn':
            break
        else:
            print('Erro',end=' ')
    if resposta in 'Nn':
        break

while True:
    print(f'-=-'*20)
    print(f'{'Code':<5}{'Nome':<15}{'Golos'}')
    for c in range(0, len(jogadores)):
        print(f'{c:<5}{jogadores[c]['Nome']:<15}{jogadores[c]['Golos']} = {jogadores[c]['Total']}')
    print(f'-=-'*20)

    while True:
        modo = int(input('Detalhes do jogador: '))
        if modo + 1 <= len(jogadores) or modo == 999:
            break
        else:
            print(f'Erro ',end='')
    
    if modo == 999:
        break
    else:
        print(f'==='*20)   
        print(f'O jogador {jogadores[modo]['Nome']} marcou um total de {jogadores[modo]['Total']} golos.')
        for i, v in enumerate(jogadores[modo]['Golos']) :
            print(f'    =» No {i+1}º jogo marcou {v} golo/s')
        print(f'==='*20)