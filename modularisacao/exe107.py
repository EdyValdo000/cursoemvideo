from moeda import moeda
número = float(input('Digite o prego: '))
print(f'O dobro de {número} é {moeda.dobro(número)}Kz')
print(f'A metade de {número} é {moeda.metade(número)}Kz')
print(f'Aumentando {10}% no preço fica {moeda.aumentar(número,10)}Kz')
print(f'Diminuindo {15}% no preço fica {moeda.diminuir(número,10)}Kz')