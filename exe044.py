print('\033[36;1m{:=^30}\033[m'.format(' Loja teste123 '))
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
    print('Vais pagar \033[32;1m{}\033[mKz nas duas parcelas do produto'.format(productPrice/2))
elif paymentMethod == 4:
    parcelas = int(input('Vais pagar quantas parcelas? '))
    productPrice20 = productPrice + (productPrice*0.2)
    print('O produto vai custar \033[1;32m{}\033[mKz e vais pagar em \033[1;32m{}\033[m parcelas um valor de \033[1;32m{}\033[mKz por parcela'.format(productPrice20, parcelas, productPrice20 / parcelas))
else:
    print('Escolhe um metodo de pagamento que existe!!!')