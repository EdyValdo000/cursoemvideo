coresDict = {
    'black': '\033[1;30;47m',   # Preto no fundo branco
    'red': '\033[1;31;40m',     # Vermelho no fundo preto
    'green': '\033[1;32;44m',   # Verde no fundo azul
    'yellow': '\033[1;33;45m',  # Amarelo no fundo roxo
    'blue': '\033[1;34;43m',    # Azul no fundo amarelo
    'purple': '\033[1;35;42m',  # Roxo no fundo verde
    'cyan': '\033[1;36;41m',    # Ciano no fundo vermelho
    'white': '\033[1;37;40m',   # Branco no fundo preto
    'none': '\033[m'                 # Reset de cores
}

resposta = função = 'S'

def printHelp(resposta=''):
    print(f'{coresDict['red']}',end='')
    help(resposta)
    print(f'{coresDict['none']}',end='')

def printEspecial(cores='green',question=True):
    print(f'{coresDict[cores]}',end='')    
    if question:
        global resposta
        resposta = str(input('Queres ajuda com que funçaõ ou biblioteca? \033[1;36m')).lower().strip()
    else:
        printHelp(resposta)
    
    print(f'{coresDict['none']}',end='')


while True:
    
    printEspecial(cores='red')    
    if resposta == 'fim':
        break    
    
    printEspecial(cores='blue',question=False)
print(f'Fim, volte sempre')