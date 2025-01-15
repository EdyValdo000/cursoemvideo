expreção = []
expreção.append(str(input('Digite uma expreção: ')))
abrir = 0
fechar = 0
primeiro = False
segundo = False

for e in range(0,len(expreção[0])):
    if expreção[0][e] == '(' and primeiro == False and segundo == False:
        primeiro = True
    if expreção[0][e] == ')':
        segundo = True
    
    if expreção[0][e] == '(':
        abrir += 1
    elif expreção[0][e] == ')':
        fechar += 1

if abrir == fechar and primeiro :
    print(f'\033[1;32mA tua expreção está boa\033[m')
else:
    print(f'\033[1;31mA tua expreção está mal\033[m')