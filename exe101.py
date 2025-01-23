from datetime import date
def voto(anoDeNascimento):
    anoActual = date.today().year
    idade = anoActual-anoDeNascimento
    resposta = f'Tens {idade} e '    
    if 65 > idade >= 18:
        resposta += 'o voto é \033[1;31mObrigatório\033[m'
    elif 18 > idade:
        resposta += 'tu \033[1;32mnão votas\033[m'
    else:
        resposta += 'o voto é \033[1;35mopcional\033[m'
    
    return resposta


anoDeNascimento = int(input('Quando é que nasceste? '))
print(voto(anoDeNascimento))