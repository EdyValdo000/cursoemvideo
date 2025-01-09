soma = num = quantidade = 0
while True:
    num = int(input(f'\033[mDigite o {quantidade + 1}º número: [999 para parar] \033[1;33m'))
    if num == 999:
        break
    soma += num
    quantidade += 1
print(f'\033[mA soma dos números é \033[1;33m{soma}\033[m, a quantidade é \033[1;33m{quantidade}\033[m.')
print('\033[1;33mFIM\033[m')