matriz = list()
linhas = []
dados = pares = valoresTerceiraColuna = maiorValorDaSegundaLinha = 0

for contador1 in range(0, 3):
    for contador2 in range(0, 3):
        dados = int(input(f'\033[mDigite o valor na posição [{contador1}, {contador2}] \033[36;1m'))
        
        if dados % 2 == 0:
            pares += dados
        
        if contador2 == 2:
            valoresTerceiraColuna += dados            

        linhas.append(dados)
    matriz.append(linhas[:])
    linhas.clear()
print('\033[m')
for contador1 in range(0, 3):
    for contador2 in range(0, 3):
        print(f'[\033[1;33m{matriz[contador1][contador2]:^10}\033[m] ',end='')
    print('')

maiorValorDaSegundaLinha = max(matriz[1])

print(f'A soma de todos os números pares é {pares}')
print(f'A soma de todos os números da terceira coluna é {valoresTerceiraColuna}')
print(f'O maior valor da segunda linha é {maiorValorDaSegundaLinha}')