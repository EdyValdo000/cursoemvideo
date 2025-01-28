def dobro(número):
    return número * 2
def metade(número):
    return número / 2
def diminuir(número,percentagem):
    return número - (número * (percentagem/100))
def aumentar(número,percentagem):
    return número + (número * (percentagem/100))
def resumo(valor,aumentou,diminuiu):    
    mais = aumentar(valor,aumentou)
    menos = diminuir(valor,diminuiu)
    metades = metade(valor)
    dobros = dobro(valor)

    print(f"-"*40)
    print(f"{"Sistema de analise de moedas":^40}")
    print(f"-"*40)
    print(f"{"O número a ser analisado é: ":<30}{valor:.2f}Kz")
    print(f"{"O dobro dele é: ":<30}{dobros:.2f}Kz")
    print(f"{"A metade dele é: ":<30}{metades:.2f}Kz")
    print(f"{f"Aumentando {aumentou}% nele fica: ":<30}{mais:.2f}Kz")
    print(f"{f"Diminuindo {diminuiu}% nele fica: ":<30}{menos:.2f}Kz")
    print(f"-"*40)