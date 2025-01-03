maior = 0.0
menor = 0.0
pesos = []
elementos = 0
for e in range(0,6):
    elementos = float(input('Digite o {}º peso em Kg: '.format(e+1)))
    pesos.append(elementos)
maior = max(pesos)
menor = min(pesos)
print('O menor peso é \033[1;31m{}\033[mKg e o maior é \033[1;36m{}\033[mKg'.format(menor, maior))