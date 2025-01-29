from ex115.cadastro import criar,ler,editar,apagar
from ex115.formatacao import titulo,fim, tabela
# Exemplo de uso
nome = "Cadastro.txt"
opções = ['Criar', 'Ler', 'Sair']
comprimento = len('============================================')
while True:
    titulo('Ben vindo ao sistema de cadastro',14)    
    while True:
        opção = tabela(opções,comprimento)
        if 0 < opção <= 3:
            break
        else:
            print('\033[1;31mErro\033[m')
    print(f'Escolheste a opção {opção}.')
    if opção == 3:
        break
fim()
    
    