def contagem (inicio, fim, passo):    
    sequência = list()
    print(f'='*55)
    print(f'Contagem de {inicio} até {abs(fim)} de {abs(passo)} em {abs(passo)}\n')
    if inicio < fim:
        for valor in range(inicio, fim+1, passo):
           sequência.append(valor) 
    elif fim < inicio:
        for valor in range(inicio, fim-1, abs(passo)*-1):
            sequência.append(valor)
    for index, valor in enumerate(sequência):
        print(f'{valor}',end=', ' if index != len(sequência)-1 else '.\n')
    print(f'='*55)


contagem(1,10,1)
contagem(10, 1, -1)
inicio = int(input(f'Início: '))
fim = int(input(f'Fim: '))
passos = int(input(f'Passos: '))
contagem(inicio,fim,passos)