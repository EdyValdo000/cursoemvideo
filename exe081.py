números = list ()
resposta = 'S'
contador = 0

while True:
    if resposta in 'Nn':
        break
    
    números.append(int(input('Digite um número: ')))
    contador += 1

    while True:
        resposta = str(input('Quer continuar? [\033[1;32mS\033[m/\033[1;31mN\033[m] ')).lower().strip()[0]
        if resposta not in 'SNsn':
            print('Erro ',end=' ')
        else:
            break    

números.sort(reverse=True)
if contador == 1:
    print(f'Tu digitaste {contador} número')    
else:
    print(f'Tu digitaste {contador} números')

print(f'Os valores ordenados na ordem decrescente: {números}')

if números.count(5) != 0:
    print(f'O número 5 está na lista que digitaste')
else:
    print(f'O número 5 não está na lista')