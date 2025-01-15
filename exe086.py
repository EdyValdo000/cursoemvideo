matriz = list()
linhas = []
dados = 0

for contador1 in range(0, 3):
    for contador2 in range(0, 3):
        dados = int(input(f'Digite o valor na posição [{contador1}, {contador2}] '))
        linhas.append(dados)
    matriz.append(linhas[:])
    linhas.clear()
print('')
for contador1 in range(0, 3):
    for contador2 in range(0, 3):
        print(f'[\033[1;33m{matriz[contador1][contador2]:^10}\033[m] ',end='')
    print('')