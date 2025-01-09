#Produto
nome = []
preço = []
leitura = nomeProdutoMaisBarato = elementoNome = ''
totalGasto = produtosMaisDe1000 = preçoProdutoMaisBarato = elementoPreço = 0
print('Bem vindo, podes digitar a lista dos pordutos que vais comprar connosco')
print('-=-'*30)
while True:    
    while True:
        elementoNome = str(input('Qual é o nome do produto? '))
        if elementoNome != '':
            break            
    nome.append(elementoNome)
    
    while True:
        elementoPreço = int(input('Qual é o preço do produto? (kz) '))
        if elementoPreço > 0:
            break    
    preço.append(elementoPreço)
    totalGasto += elementoPreço
    
    while True:
        leitura = str(input('Quer continuar? [\033[1;32mS\033[m/\033[1;31mN\033[m] ')).upper().strip()[0]
        if leitura in 'SNsn':
            break
    
    if leitura in 'Nn':        
        preçoProdutoMaisBarato = elementoPreço
        nomeProdutoMaisBarato = elementoNome       
        print('{:-^40}'.format('FIM DO PROGRAMA'))
        break  
    
    print('-=-'*30)  

for e in range(0,len(preço)):
    if preço[e] > 1000:
        produtosMaisDe1000 += 1
    
    if preço[e] < preçoProdutoMaisBarato:
        preçoProdutoMaisBarato = preço[e]
        nomeProdutoMaisBarato = nome[e]    
   
    
print(f'\nTu gastaste um total de \033[1;32m{totalGasto}\033[mKz')
if produtosMaisDe1000 == 0:
    print(f'Não tem produtos que custam mais de 1000Kz')
elif produtosMaisDe1000 == 1:
    print(f'Tem \033[1;32m{produtosMaisDe1000}\033[m produto que custam mais de 1000Kz')
else:
    print(f'Tem \033[1;32m{produtosMaisDe1000}\033[m produtos que custam mais de 1000Kz')

if nomeProdutoMaisBarato[-1].lower() == 'a':
    print(f'O produto mais barato é a \033[1;32m{nomeProdutoMaisBarato}\033[m, que custa \033[1;32m{preçoProdutoMaisBarato}\033[mKz')
else:
    print(f'O produto mais barato é o \033[1;32m{nomeProdutoMaisBarato}\033[m, que custa \033[1;32m{preçoProdutoMaisBarato}\033[mKz')
print('FIM')