def lerDinehiro():
    while True:
        dinheiro = str(input("Digite um valor monetário: "))
        if dinheiro.isnumeric():
            break
        elif dinheiro.count(",") == 1 and dinheiro.count(".") == 0:
            dinheiro = dinheiro.replace(",",".")            
            break
        elif dinheiro.count(".") == 1 and dinheiro.count(",") == 0:            
            break
        else:
            print(f"\033[1;31mErro o valor \033[1;33m{dinheiro}\033[1;31m não é um valor valido\033[m")

    return float(dinheiro)