números = []
resposta = 'S'
elemento = 0

while True:
    if resposta in 'Nn':
        break
    
    elemento = int(input('Digite um número: '))
    
    if elemento not in números:
        números.append(elemento)
    else:
        print(f'\033[1;31mValor duplicado, não adicionei\033[m',end=' ')

    while True:
        resposta = str(input('Quer continuar? [\033[1;32mS\033[m/\033[1;31mN\033[m] ')).lower().strip()[0]
        if resposta not in 'SNsn':
            print('Erro ',end=' ')
        else:
            break    

números.sort()
print(f'Os valores ordenados são {números}')