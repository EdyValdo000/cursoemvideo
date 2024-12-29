number = int(input('Digite um número entre 0 e 9999: '))

unidade = number % 10
dezena = (number // 10) % 10
centena = (number // 100) % 10
milhar = (number // 1000) % 10

print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))