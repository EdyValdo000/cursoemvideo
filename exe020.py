from random import shuffle
aluno1 = input('Nome do 1º aluno: ')
aluno2 = input('Nome do 2º aluno: ')
aluno3 = input('Nome do 3º aluno: ')
aluno4 = input('Nome do 4º aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print('A sequência dos alunos que vão apresentar os trabalhos são: \033[1;36m{}\033[m'.format(", ".join(alunos)))