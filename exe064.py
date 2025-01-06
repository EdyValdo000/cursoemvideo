#ler vários números e parar com 999
#Apresentar a soma deles
#Apresentar quantos números foram lidos, sem contar com a flai
num = soma = contador = 0
num = int(input('\033[mDigite o {}º número [999 parar] \033[36;1m'.format(contador+1)))
while num != 999:
    contador += 1
    soma += num
    num = int(input('\033[mDigite o {}º número [999 parar] \033[36;1m'.format(contador+1)))
print('\033[mTu digitaste {} números, e a soma desses números é de {}'.format(contador,soma))