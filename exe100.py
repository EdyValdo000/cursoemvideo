from random import randint

def sortear(lista):
    for c in range(0,5):
        lista.append(randint(1,10))


def somaPar(lista,somar):
    for valor in lista:
        if valor % 2 == 0:
            somar += valor
    print(f'A sequencia de números é',end=' ')
    números.sort()
    for index, valor in enumerate(números):
        print(f'{valor}',end=', ' if index != (len(números)-1) else '.\n')
    print(f'A soma dos números pares é {somar}.')


números = list()
soma = 0
sortear(números)
somaPar(números,soma)