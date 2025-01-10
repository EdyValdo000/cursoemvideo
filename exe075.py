pares = 0
números = (int(input('Digite o 1º valor: ')), 
    int(input('Digite o 2º valor: ')), 
    int(input('Digite o 3º valor: ')), 
    int(input('Digite o 4º valor: ')))

print(f'Tu digitaste os números {números}')

if números.count(9) == 1:
    print(f'O número 9 apareceu {números.count(9)} vez')
elif números.count(9) >= 2:
    print(f'O número 9 apareceu {números.count(9)} vezes')
else:
    print(f'O número 9 não apareceu')

if números.count(3) != 0:
    print(f'O número 3 está na {números.index(3) + 1}ª posição')
else:
    print(f'O número 3 não foi digitado')

for e in números:
    if e % 2 == 0:
        pares += 1

if pares == 0:
    print('Não digitaste nenhum número par')
elif pares == 1:
    for e in números:
        if e % 2 == 0:
            print(f'O único número par que digitaste é {e}')
else:
    print(f'Os números pares que digitaste são: ',end='')
    for e in números:        
        if e % 2 == 0:
            print(f'{e}',end='; ')
print('\nFIM')