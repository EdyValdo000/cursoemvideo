def ficha(nome='', Golos=''):
    resposta = ''
    if nome == '':
        nome = '<desconhecido>'    
    
    if  Golos.isalpha or Golos == '':
        golos = 0
    else:
        golos = Golos

    if golos != 1:
        resposta =  f'O jogador \033[33;1m{nome}\033[m marcou \033[33;1m{golos}\033[m golos no campeonato'
    else:
        resposta =  f'O jogador \033[33;1m{nome}\033[m marcou \033[33;1m{golos}\033[m golo no campeonato'    
    return resposta


Nome = str(input('Nome do jogador: '))
Golos = str(input('Números de golos: ')).replace(' ','')
print(f'{ficha(Nome,Golos)}')

