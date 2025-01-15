números = list()
pares = []
impares = []
número = 0
for c in range(1,8):
    número = int(input(f'Digite o {c}º número: '))
    if número % 2 == 0:
        pares.append(número)
    elif número % 2 != 0:
        impares.append(número)

pares.sort()
impares.sort()
números.append(pares)
números.append(impares)

for i, valor1 in enumerate(números):
    if i == 0:
        print(f'Os números pares são ',end='')
    else:
        print(f'\nOs números impares são ',end='')
    for index, valor2 in enumerate(números[i]):
        print(f'{valor2}', end='.' if index + 1 == len(números[i]) else ', ')
