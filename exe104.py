def leituraInt(mensagemDeEntrada='Digite um valor numérico'):
    """
    Essa função vai manter um loop até ler um valor numérico
    """
    while True:
        número = input(f'{mensagemDeEntrada} ')
        if número.isnumeric():            
            return número
        else:
            print(f'\033[1;31mErro o valor "\033[1;33m{número}\033[1;31m" não é um número\033[m')


número = leituraInt()
print(f'\033[32;1mTu digitaste o número {número}\033[m')
