valor = float(input('Qual é o preço do produto? '))
desconto = valor * 0.05
newValor = valor - desconto
print('O desconto foi de {:.2f}Kz e o novo valor é {:.2f}Kz'.format(desconto,newValor))