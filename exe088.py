from random import randint
jogos = list()
sorteados = []
númeroDeJogos = 0
dado = 0

númeroDeJogos = int(input('Vais precisar de quantos jogos? '))

for e in range(0, númeroDeJogos):
    while True:
        dado = randint(1,60)
        if dado not in sorteados:
            sorteados.append(dado)    
        if len(sorteados) == 6:
            sorteados.sort()
            jogos.append(sorteados[:])
            sorteados.clear()
            break    

for index1, valor1 in enumerate(jogos):
    print(f'Jogo {index1+1} ( ', end='')
    for index2, valor2 in enumerate(jogos[index1]):
        print(f'{jogos[index1][index2]}',end=', ' if index2 != 5 else ' )\n')