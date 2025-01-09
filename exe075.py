número_1º = int(input('Digite o 1º valor: '))
número_2º = int(input('Digite o 2º valor: '))
número_3º = int(input('Digite o 3º valor: '))
número_4º = int(input('Digite o 4º valor: '))
pares = 0
números = (número_1o, número_2o, número_3o, número_4o)

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
        

if pares != 0 and pares != 1:
    print(f'Tu digitaste {pares} número par')
elif pares >= 2:
    print(f'Tu digitaste {pares} números pares')
else:
    print(f'Tu não digitaste nenhum número par')