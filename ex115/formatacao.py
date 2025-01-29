def titulo(txt='Título',comprimento = 8):
    print(f'='*(len(txt)+comprimento))
    print(f'{txt:^{len(txt)+comprimento}}')

def fim():
    titulo('Volte sempre...',32)

def tabela(opções,comprimento=8):
    print(f'='*(len(opções)+comprimento))
    print('Opções validas:')
    for index, valor in enumerate(opções):
        print(f'{index+1})\t{valor}')    
    print(f'='*(len(opções)+comprimento))
    return leituraInt('Escolha uma: ')

def leituraInt(mensagemDeEntrada='Digite um valor inteiro'):
    """
    Essa função vai manter um loop até ler um valor numérico do tipo int
    """
    while True:
        try:        
            número = int(input(f'{mensagemDeEntrada} '))

        except (ValueError,TypeError):
            print("\033[1;31mO valor inteiro não é valido\033[m")
        
        except Exception:
            print(f'Deu um erro do tipo {Exception.__class__}')
        
        else:
            return número