termo = int(input('1º termo da PA: '))
razão = int(input('Razão da PA: '))
valor = 10
limTermo = termo + (valor - 1)*razão
while termo <= limTermo:
    print(termo,end='; ')
    termo += razão   
print('FIM')