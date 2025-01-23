def ficha(nome='', golos=0):
    resposta = ''
    if nome == '':
        nome = '<desconhecido>'
    
    if golos != 1:
        resposta =  f'O jogador \033[33;1m{nome}\033[m marcou \033[33;1m{golos}\033[m golos no campeonato'
    else:
        resposta =  f'O jogador \033[33;1m{nome}\033[m marcou \033[33;1m{golos}\033[m golo no campeonato'    
    return resposta

print(f'{ficha()}')
