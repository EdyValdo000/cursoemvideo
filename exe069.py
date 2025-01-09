leitura = elementoSexo = ''
elementoIdade = maioresDe18 = númeroDeHomens = númeroDeMulheresMenoresDe20 = 0
idade = [0]
sexo = ['']
while True:
    elementoIdade = int(input('\033[mDigita a tua idade: \033[1;33m'))
    idade.append(elementoIdade)
    if elementoIdade > 18:
        maioresDe18 += 1
    while True:
        elementoSexo = str(input('\033[mDigita o seu sexo [\033[1;31mM\033[m/\033[1;35mF\033[m]: ')).upper().strip()[0]
        if elementoSexo in 'MFmf':
            break
    sexo.append(elementoSexo)
    while True:
        leitura = str(input('\033[mQueres continuar a ler valores? [\033[1;32mS\033[m/\033[1;31mN\033[m]: '))
        if leitura in 'SNsn':
            break
    if leitura in 'Nn':
        break
    print('-=-'*25)

for e in range(0,len(sexo)):
    if sexo[e] == 'M':
        númeroDeHomens += 1
for e in range(0,len(sexo)):
    if sexo[e] == 'F' and idade[e] < 20:
        númeroDeMulheresMenoresDe20 += 1        

if maioresDe18 == 0:
    print(f'Não tem ninguém com mais de 18 anos.') 
elif maioresDe18 == 1:
    print(f'Tem \033[1;35m{maioresDe18}\033[m pessoa com mais de 18 anos.')
else:   
    print(f'Tem \033[1;35m{maioresDe18}\033[m pessoas com mais de 18 anos.')

if númeroDeHomens == 0:
    print(f'Tu não registatste nenhum homem.')
elif númeroDeHomens == 1:
    print(f'Tu registatste \033[1;35m{númeroDeHomens}\033[m homem.')    
else:
    print(f'Tu registatste \033[1;35m{númeroDeHomens}\033[m homens.')

if númeroDeMulheresMenoresDe20 == 0:
    print(f'Não tem nenhuma mulheres com menos de 20 anos')
elif númeroDeMulheresMenoresDe20 == 1:
    print(f'Tem \033[1;35m{númeroDeMulheresMenoresDe20}\033[m mulher com menos de 20 anos')
else:
    print(f'Tem \033[1;35m{númeroDeMulheresMenoresDe20}\033[m mulheres com menos de 20 anos')
print('FIM')