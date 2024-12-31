number = int(input('Digite um número entre 0 e 9999: '))

unidade = number % 10
dezena = (number // 10) % 10
centena = (number // 100) % 10
milhar = (number // 1000) % 10

print('Unidade: \033[7;35;43m{}\033[m'.format(unidade))
print('Dezena: \033[7;35;43m{}\033[m'.format(dezena))
print('Centena: \033[7;35;43m{}\033[m'.format(centena))
print('Milhar: \033[7;35;43m{}\033[m'.format(milhar))