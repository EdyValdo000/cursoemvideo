contador = 0
produtos = ('Pão', 50, 'Arroz', 5000, 'Massa', 300, 'Abacate', 100)
print('-'*30)
print('{:^30}'.format(' LISTA DE PRODUTOS '))
print('-'*30)
while contador < len(produtos):
    print(f'{produtos[contador]:.<20}',end='')
    print(f'{produtos[contador+1]:.>6} {'Kz':>3}')
    contador += 2
print('-'*30)