frase = input('Digite a frase: ')
teste = False
for e in range(0,len(frase)):
    if frase[e].replace(' ','').lower() == frase[len(frase) - e -1].replace(' ','').lower():
        teste = True
    else:
        teste = False
if teste:
    print('\033[1;32mA frase é um palindromo\033[m')
else:
    print('\033[1;31mA frase não é um palindromo\033[m')

print('A frase ao contrário é \033[1;36m',end=' ')
for e in range(len(frase)-1,-1,-1):
    print(frase[e],end='')
print('\n\033[mE normal é \033[1;36m{}\033[m'.format(frase))