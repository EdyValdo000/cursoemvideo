contador = 0
produtos = ('Pão', 50, 'Arroz', 5000, 'Massa', 300, 'Abacate', 100)
print('-'*40)
print('{:^30}'.format(' LISTA DE PRODUTOS '))
print('-'*40)
while contador < len(produtos):
    print(f'{produtos[contador]:.<20}',end='')
    print(f'{produtos[contador+1]:.>10.2f} {'Kz':>3}')
    contador += 2
print('-'*40)