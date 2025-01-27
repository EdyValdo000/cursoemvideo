import ex107.moeda
import ex108.formatacao

def aumentar(valor, percentagem, formated=False):
    if formated:
        valor = ex107.moeda.aumentar(valor,percentagem)
        return ex108.formatacao.Moeda(valor)
    else:
        return ex107.moeda.aumentar(valor,percentagem)
    

def diminuir(valor, percentagem, formated=False):
    if formated:
        valor = ex107.moeda.diminuir(valor,percentagem)
        return ex108.formatacao.Moeda(valor)
    else:
        return ex107.moeda.diminuir(valor,percentagem)
    

def dobro(valor,formated=False):
    if formated:
        valor = ex107.moeda.dobro(valor)
        return ex108.formatacao.Moeda(valor)
    else:
        return ex107.moeda.dobro(valor)
    

def metade(valor, formated=False):
    if formated:
        valor = ex107.moeda.metade(valor)
        return ex108.formatacao.Moeda(valor)
    else:
        return ex107.moeda.metade(valor)  
    

def formatarMoeda(valor,sim=False):
    if sim:
        return str(valor)+'Kz'
    else:
        return valor