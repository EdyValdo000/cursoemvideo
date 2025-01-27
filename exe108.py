from ex107 import moeda
from ex108 import formatacao

número = float(input('Digite o preço: '))

mais = 15
menos = 10

aumento = formatacao.Moeda(moeda.aumentar(número,mais))
diminuido = formatacao.Percentagem(moeda.diminuir(número,menos))
metade = formatacao.Moeda(moeda.metade(número))
dobro = formatacao.Moeda(moeda.dobro(número))

print(f'Com o aumeto de {formatacao.Percentagem(mais)} no preço ele vai para {aumento}')
print(f'Com o desconto de {formatacao.Percentagem(mais)} no preço ele vai para {diminuido}')
print(f'O dobro de {número} é {dobro}')
print(f'A metade de {número} é {metade}')