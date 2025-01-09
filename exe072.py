contagem = ('zero', 'um', 'dois', 'três', 
            'quatro', 'cinco', 'seis', 
            'sete', 'oito', 'nove', 
            'dez', 'onze', 'doze', 
            'treze', 'quatorze', 'quinze', 
            'dezaseis', 'dezessete', 'dezoito', 
            'dezenove', '\033[1;33mvinte\033[m')
número = int(input('Digite um número: '))
while True:
    if not 0 <= número <= 20:
        número = int(input('Tente novamente, digite um número: '))
    else:
        print(f'Tu digitaste o número {contagem[número]}')
        break