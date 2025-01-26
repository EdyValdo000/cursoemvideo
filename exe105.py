def notas(*notas,includeSituation=False):
    turma = dict()
    totalNotas = len(notas)
    maiorNota = max(notas)
    menorNota = min(notas)
    média = sum(notas) / len(notas)
    
    turma['Total'] = totalNotas
    turma['Maior'] = maiorNota
    turma['Menor'] = menorNota
    turma['Média'] = f'{média:.2f}'

    if includeSituation:
        if 0 <= média < 10:
            turma['Situação'] = 'RUIN'
        elif 10 <= média < 11:
            turma['Situação'] = 'RASUAVEL'
        elif média >= 20:
            turma['Situação'] = 'MUITO BOA'
        else:
            turma['Situação'] = 'BOA'
    return turma


turma = dict()
turma = notas(10,10,10,10,20,10,20,includeSituation=True)
print(f'{turma}')