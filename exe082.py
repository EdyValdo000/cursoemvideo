números = []
resposta = 'S'
pares = []
impares = []

while True:
    if resposta in 'Nn':
        break
    
    números.append(int(input('Digite um número: ')))

    while True:
        resposta = str(input('Quer continuar? [\033[1;32mS\033[m/\033[1;31mN\033[m] ')).lower().strip()[0]
        if resposta not in 'SNsn':
            print('Erro ',end=' ')
        else:
            break    
for e in números:
    if e % 2 == 0:
        pares.append(e)
    else:
        impares.append(e)

print(f'A lista completa é essa:\n{números}')
print(f'A lista dos números pares é essa:\n{pares}')
print(f'A lista dos números impares é essa:\n{impares}')