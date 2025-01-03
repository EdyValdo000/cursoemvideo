termo = int(input('Digite o 1º termo da PA: '))
razão = int(input('Digite a razão da PA: '))
for e in range(termo,termo + razão*10,razão):
    print(e,end='; ')