n = 1
par = inpar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0 and n != 0:
        par += 1
    elif n % 2 != 0 and n != 0:
        inpar += 1
print('Digitaste {} números pares e {} números impares'.format(par,inpar))