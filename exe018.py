from math import sin,cos,tan,radians
angle = int(input('Digite um algulo: '))
angleRad = radians(angle)
seno = sin(angleRad)
cosseno = cos(angleRad)
tangente = tan(angleRad)
print('O seno(\033[1;31m{}º\033[m) = \033[1;36m{:.2f}\033[m'.format(angle,seno))
print('O cos(\033[1;31m{}º\033[m) = \033[1;36m{:.2f}\033[m'.format(angle,cosseno))
print('A tg(\033[1;31m{}º\033[m) = \033[1;36m{:.2f}\033[m'.format(angle,tangente))