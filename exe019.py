from random import choicey
aluno1 = input('Nome do 1º aluno: ')
aluno2 = input('Nome do 2º aluno: ')
aluno3 = input('Nome do 3º aluno: ')
aluno4 = input('Nome do 4º aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
print('O aluno que vai limpar o quadro é: {}'.format(choicey(alunos)))