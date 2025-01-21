jogador = dict()
golos = list()
golosElementos = []
jogador ['Nome'] = str(input('Nome do jogador: '))
partidas = totalGolos = 0
partidas = int(input(f'Quantas partidas o {jogador["Nome"]} jogou: '))

for c in range(1,partidas+1):
    golosElementos = int(input(f'No {c}º jogo marcou quantos golos? '))
    totalGolos += golosElementos
    golos.append(golosElementos)
jogador['Golos'] = golos
jogador['Total'] = totalGolos

print(f'\n{jogador}\n')

print(f'O {jogador['Nome']} teve um resultado\n')
for i, v in enumerate(jogador['Golos']):
    print(f'    =>No jogo {i+1} marcou {v}')
print(f'E marcou um total de {totalGolos} golos')