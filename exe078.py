números = []
posMaior = []
posMenor = []
maior = menor = 0
for e in range(1,6):
    números.append(int(input(f'\033[mDigite o {e}º valor: \033[1;33m')))

maior = max(números)
if números.count(maior) > 1:
    for i, e in enumerate(números):
        if e == maior:
           posMaior.append(i)
            
menor = min(números)
if len(números) > 1:
    for i, e in enumerate(números):
        if e == menor:
            posMenor.append(i)

if len(posMaior) > 1 and len(posMaior) != 5:
    print(f'\033[mO maior valor é {maior} e está nas posições {posMaior}')    
elif len(posMaior) == 1:
    print(f'\033[mO maior valor é {maior} e está na posição {posMaior}')

if len(posMenor) > 1 and len(posMenor) != 5:
    print(f'\033[mO menor valor é {menor} e está nas posições {posMenor}')    
elif len(posMenor) == 1:
    print(f'\033[mO menor valor é {menor} e está na posição {posMenor}')
else:
    print(f'\033[1;36mTodos os números são iguais\033[m')