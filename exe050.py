soma = 0
contador = 0
for e in range(0,6):
    num = int(input('Digite um número interio: '))
    if num % 2 == 0:
        soma += num
        contador += 1
print('A soma dos {} números pares que digitaste é {}'.format(contador,soma))