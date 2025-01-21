def área(*segmentos):
    print(f'A área do seu terreno de {segmentos[0]} * {segmentos[1]} é de {segmentos[0]*segmentos[1]}m²')


# Principal
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
área(largura, comprimento)
