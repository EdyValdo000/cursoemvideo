from ex107 import moeda

def resumo(valor,aumentou,diminuiu):    
    mais = moeda.aumentar(valor,aumentou)
    menos = moeda.diminuir(valor,diminuiu)
    metades = moeda.metade(valor)
    dobros = moeda.dobro(valor)

    print(f"-"*40)
    print(f"{"Sistema de analise de moedas":^40}")
    print(f"-"*40)
    print(f"{"O número a ser analisado é: ":<30}{valor}Kz")
    print(f"{"O dobro dele é: ":<30}{dobros}Kz")
    print(f"{"A metade dele é: ":<30}{metades}Kz")
    print(f"{f"Aumentando {aumentou}% nele fica: ":<30}{mais}Kz")
    print(f"{f"Diminuindo {diminuiu}% nele fica: ":<30}{menos}Kz")
    print(f"-"*40)