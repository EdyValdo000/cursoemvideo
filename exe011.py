largura = float(input('Qual é a largura da parede? '))
comprimento = float(input('Qual é o comprimento da parede? '))
area = largura * comprimento
refArea = 2
refLitro = 1
litro = (area * refLitro) / refArea

print('Para pintar \033[1;35m{}\033[m metros quadrados vais precisar de \033[1;36m{}L\033[m de tinta'.format(area,litro))