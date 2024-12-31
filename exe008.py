metro = float(input('Digite a distancia em metros (m): '))
km = metro / 1000
cm = metro * 100
mm = metro * 1000

print('A distancia de \033[1;30m{}\033[mm em centimetros é \033[1;31m{}\033[mcm em milimetros é \033[1;32m{}\033[mmm e em kilometro é \033[1;33m{}\033[mKm são esses.'.format(metro,cm,mm,km))