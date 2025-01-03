from datetime import date
ano = date.today().year
maior = 0
menor = 0
maiorIdade = 21
for e in range(1,8):
    anoNascimento = int(input('\033[1;32mDigite o {}º ano: \033[m\033[1;33m'.format(e)))
    idade = ano - anoNascimento
    if idade >= maiorIdade:
        maior = maior + 1
    else:
        menor = menor + 1
if maior == 1 and menor > 1:
    print('\033[1;32mEm função das datas que digitaste tinha \033[1;33m{}\033[1;32m maior de {}, e \033[1;33m{}\033[1;32m menores de {}\033[m'.format(maior,maiorIdade,menor,maiorIdade))
elif menor == 1 and maior > 1:
    print('\033[1;32mEm função das datas que digitaste tinha \033[1;33m{}\033[1;32m maiores de {}, e \033[1;33m{}\033[1;32m menor de {}\033[m'.format(maior,maiorIdade,menor,maiorIdade))    
elif maior == menor == 1:
    print('\033[1;32mEm função das datas que digitaste tinha \033[1;33m{}\033[1;32m maior de {}, e \033[1;33m{}\033[1;32m menor de {}\033[m'.format(maior,maiorIdade,menor,maiorIdade))
else:
    print('\033[1;32mEm função das datas que digitaste tinha \033[1;33m{}\033[1;32m maiores de {}, e \033[1;33m{}\033[1;32m menores de {}\033[m'.format(maior,maiorIdade,menor,maiorIdade))