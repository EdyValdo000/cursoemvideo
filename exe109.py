from ex109 import aumentar,diminuir,dobro,metade,formatarMoeda
número = int(input('Digite um número: '))
PercentagemAumento = 10
PercentagemDiminui = 15


print(f'O dobro de {formatarMoeda(número,True)} é {dobro(número,True)}')
print(f'A metade de {formatarMoeda(número,True)} é {metade(número,True)}')
print(f'Aumentando {PercentagemAumento}% no preço fica {aumentar(número,PercentagemAumento,True)}')
print(f'Diminuindo {PercentagemDiminui}% no preço fica {diminuir(número,PercentagemDiminui,True)}')