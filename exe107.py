from ex107 import moeda
número = float(input('Digite o prego: '))
print(f'O dobro de {número} é {moeda.dobro(número)}')
print(f'A metade de {número} é {moeda.metade(número)}')
print(f'Aumentando {10} no preço fica {moeda.aumentar(número,10)}')
print(f'Diminuindo {15} no preço fica {moeda.diminuir(número,10)}')