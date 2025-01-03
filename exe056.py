nomes = []
idades = []
sexos = []
soma = 0
homemMaisVelho = '' 
idadeDoMaisVelho = 0
numeroDeMulheres = 0

for e in range(0,4):
    nomeVariavel = str(input('{}º nome: '.format(e+1))).strip()
    nomes.append(nomeVariavel)
    idadeVariavel = int(input('{}ª idade: '.format(e+1)))
    idades.append(idadeVariavel)
    print('Sobre os sexos \033[35;1mF\033[m femenino e \033[1;31mM\033[m masculino')
    sexosVariaveis = input('{}º sexo: '.format(e+1))    
    sexos.append(sexosVariaveis)    
    print('\033[1;33m-=-\033[m'*15)

    if sexos[e].upper() == 'M':
        if idadeDoMaisVelho < idades[e]:
            idadeDoMaisVelho = idades[e]
            homemMaisVelho = nomes[e]
    if sexos[e].upper() == 'F' and idades[e] < 20:
        numeroDeMulheres += 1
    soma += idades[e]   
    
print('A média de idades é \033[1;36m{}\033[m'.format(soma/4))
print('O homem mais velho é o \033[1;36m{}\033[m com \033[1;36m{}\033[m anos'.format(homemMaisVelho,idadeDoMaisVelho))
if numeroDeMulheres == 1:
    print('Tem \033[1;36m{} mulhere\033[m com menos de 20 anos'.format(numeroDeMulheres))    
else:
    print('Tem \033[1;36m{} mulheres\033[m com menos de 20 anos'.format(numeroDeMulheres))