Alunos = list() # vai receber append ----- [aluno]
aluno = [] # vai receber append ----- [nome, Notas]
Notas= [] # vai receber append ----- [p1,p2]
p1 = p2 = média = 0
nome = ''
resposta = 'S'
while True:
    nome = str(input('Nome: '))
    p1 = int(input('Nota 1: '))
    p2 = int(input('Nota 2: '))

    Notas.append(p1)
    Notas.append(p2)
    aluno.append(nome)
    aluno.append(Notas[:])
    Alunos.append(aluno[:])

    Notas.clear()
    aluno.clear()

    while True:
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SsNn':
            break
    
    if resposta in 'Nn':
        break

# Alunos = [['Maria', [15,16]], ['Maria', [15,16]], ['Maria', [15,16]],[ 'Maria', [15,16]] ]
print('-='*35)
print(f'{'No.':<7}{'NOME':<25}{'MÉDIAS':}')
print('--'*35)
for index, aluno in enumerate(Alunos):
    média = (aluno[1][0] + aluno[1][1]) / 2
    print(f'{index:<7}{aluno[0]:<25}{média:.1f}')