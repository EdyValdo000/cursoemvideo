elementos = med = maior = menor = contador = soma = 0
num = []
continuar = 'S'
while continuar == 'S':
    elementos = int(input('Digite o {}º número: '.format(contador+1)))
    contador += 1
    soma += elementos
    num.append(elementos)
    continuar = 'S'
    continuar = str(input('Queres continuar? \033[32;1m[S]\033[m ou \033[31;1m[N]\033[m: ')).upper().strip()

med = soma / contador
maior = max(num)
menor = min(num)

print('A \033[1;36mmédia dos valores que digitaste é\033[m {} \033[1;36mo maior valor é\033[m {} \033[1;36me o menor é\033[m {}'.format(med,maior,menor))