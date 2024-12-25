largura = float(input('Qual é a largura da parede? '))
comprimento = float(input('Qual é o comprimento da parede? '))
area = largura * comprimento
refArea = 2
refLitro = 1
litro = (area * refLitro) / refArea

print('Para pintar {} metros quadrados vais precisar de {}L de tinta'.format(area,litro))