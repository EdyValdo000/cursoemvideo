productPrice = float(input('Digite o preço do produto: '))
paymentMethod = int(input("""Qual é o modo de pagamento que vais escolher?
1-->À vista \033[34;1mdinheiro/cheque\033[m: Desconto \033[33;1m10%\033[m de desconto
2-->À vista no \033[34;1mcartão\033[m: Desconto \033[33;1m5%\033[m de desconto
3-->Em até \033[34;1m2x no cartão\033[m: preço normal
4-->\033[34;1m3x ou mais\033[m no cartão: \033[33;1m20%\033[m de juros\n"""))
if paymentMethod == 1:
    print('Vais pagar \033[32;1m{}\033[mKz pelo produto'.format(productPrice - (productPrice*0.1)))
elif paymentMethod == 2:
    print('Vais pagar \033[32;1m{}\033[mKz pelo produto'.format(productPrice - (productPrice*0.05)))
elif paymentMethod == 3:
    print('Vais pagar \033[32;1m{}\033[mKz pelo produto'.format(productPrice))
elif paymentMethod == 4:
    print('Vais pagar \033[32;1m{}\033[mKz pelo produto'.format(productPrice + (productPrice*0.2)))
else:
    print('Escolhe um metodo de pagamento que existe!!!')