from math import sin,cos,tan,radians
angle = int(input('Digite um algulo: '))
angleRad = radians(angle)
seno = sin(angleRad)
cosseno = cos(angleRad)
tangente = tan(angleRad)
print('O seno({}) = {:.2f}'.format(angle,seno))
print('O cos({}) = {:.2f}'.format(angle,cosseno))
print('A tg({}) = {:.2f}'.format(angle,tangente))