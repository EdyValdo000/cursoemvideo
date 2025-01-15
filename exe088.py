from random import randint
jogos = list()
sorteados = []
númeroDeJogos = 0
dado = 0

númeroDeJogos = int(input('Vais precisar de quantos jogos? '))

for e in range(0, númeroDeJogos):
    while True:
        dado = randint(0,60)
        if dado not in sorteados:
            sorteados.append(dado)    
        if len(sorteados) == 6:
            sorteados.sort()
            jogos.append(sorteados[:])
            sorteados.clear()
            break
    print(f'Jogo {e+1} {jogos[e]}')