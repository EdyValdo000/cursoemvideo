valor = float(input('Qual é o preço do produto? '))
desconto = valor * 0.05
newValor = valor - desconto
print('O produto que custava {:.2f}Kz depois do desconto de 5 porcentos ele agora custa {:.2f}Kz'.format(valor,newValor))