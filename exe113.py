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


def leituraFloat(mensagemDeEntrada='Digite um valor real'):
    """
    Essa função vai manter um loop até ler um valor numérico do tipo float
    """
    while True:
        try:        
            número = float(input(f'{mensagemDeEntrada} '))

        except (ValueError,TypeError):
            print("\033[1;31mO valor inteiro não é valido\033[m",end='. ')
        
        except Exception:
            print(f'Deu um erro do tipo {Exception.__class__}',end='. ')
        
        else:
            return número
        

númeroInt = leituraInt()
númeroFloat = leituraFloat()
print(f'O snúmeros que digitaste foram {númeroInt} e {númeroFloat}')