soma = 0
contador = 0
for e in range(0,501, 3):
   if e % 2 != 0:
        soma += e
        contador += 1
print('A soma de todos os \033[1;32m{}\033[m números primos que são multiplos de 3 de [1;500] é de \033[1;32m{}\033[m'.format(contador,soma))