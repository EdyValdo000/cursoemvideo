import uteis.numeros
num = int(input('Digite um número: '))
fat = uteis.numeros.factorial(num)
print(f'O factorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.numeros.dobro(num)}')