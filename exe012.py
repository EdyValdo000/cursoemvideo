valor = float(input('Qual é o preço do produto? '))
desconto = valor * 0.05
newValor = valor - desconto
print('\033[1;31mO produto que custava {:.2f}Kz depois do desconto de 5 porcentos ele agora custa {:.2f}Kz\033[m'.format(valor,newValor))