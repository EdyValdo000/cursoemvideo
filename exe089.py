Alunos = list() # vai receber append ----- [aluno]
aluno = [] # vai receber append ----- [nome, Notas]
Notas= [] # vai receber append ----- [p1,p2]
p1 = p2 = média = númeroAluno = 0
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
    if aluno[0][-1] in 'AaUu':
        print(f'{index:<7}\033[1;35m{aluno[0]:<25}', end='\033[33;1m' if média >= 10 else '\033[1;31m')
        print(f'{média}\033[m')
    else:
        print(f'{index:<7}\033[1;32m{aluno[0]:<25}', end= '\033[33;1m' if média >= 10 else '\033[31;1m')
        print(f'{média}\033[m')
    
print('')
while True:
    númeroAluno = int(input('Qual é a posição do aluno que queres ver as notas? [999 para parar] '))
    if númeroAluno == 999:
        break
    elif númeroAluno < len(Alunos):
        if Alunos[númeroAluno][0][-1] in 'AaUu':
            print(f'A \033[1;35m{Alunos[númeroAluno][0]}\033[m teve P1 =','\033[1;33m' if Alunos[númeroAluno][1][0] >= 10 else '\033[31;1m',f'{Alunos[númeroAluno][1][0]}\033[m P2 =','\033[1;33m' if Alunos[númeroAluno][1][1] >= 10 else '\033[1;31m',f'{Alunos[númeroAluno][1][1]}\033[m\n')
        else:
            print(f'O \033[1;32m{Alunos[númeroAluno][0]}\033[m teve P1 =','\033[1;33m' if Alunos[númeroAluno][1][0] >= 10 else '\033[1;31m',f'{Alunos[númeroAluno][1][0]}\033[m P2 =','\033[1;33m' if Alunos[númeroAluno][1][1] >= 10 else '\033[1;31m',f'{Alunos[númeroAluno][1][1]}\033[m\n')
    else:
        print('\033[1;31mErro \033[m',end='')
print('FIM')