controlo = leituraDeNúmeros = True
num = [0,0]
multiplicação = 1
elemento = modo = soma = maior = 0
while controlo:
    if leituraDeNúmeros:
        print('\033[33;1m-=-\033[m'*15)
        for e in range(0,2):
            elemento = int(input('Digite o {}º número: '.format(e+1)))
            num[e] = elemento
            leituraDeNúmeros = False
    print('\033[33;1m-=-\033[m'*15)
    print("""[1] Somar\n[2] Multiplicar\n[3] Maior número\n[4] Novos números\n[5] Sair do programa""")
    print('\033[33;1m-=-\033[m'*15)
    modo = int(input('Escolhe uma opção: '))

    if modo == 1:
        for e in range(0,len(num)):
            soma += num[e]
        print('\033[36;1m-=-\033[m'*15)
        print('O resultado da soma de {}+{} = {}'.format(num[0],num[1],soma))
        print('\033[36;1m-=-\033[m'*15)
    elif modo == 2:
        for e in range(0,len(num)):
            multiplicação *= num[e]
        print('\033[36;1m-=-\033[m'*15)
        print('O resultado da multiplicação de {}+{} = {}'.format(num[0],num[1],multiplicação))
        print('\033[36;1m-=-\033[m'*15)
    elif modo == 3:
        maior = max(num)
        print('\033[36;1m-=-\033[m'*15)
        print('O maior número entre {} e {} é {}'.format(num[0],num[1],maior))
        print('\033[36;1m-=-\033[m'*15)
    elif modo == 4:
        controlo = True
        leituraDeNúmeros = True
        print('\n')
    elif modo == 5:
        controlo = False
        print('\033[36;1m-=-\033[m'*15)
        print('FIM do programa, volte sempre')
        print('\033[36;1m-=-\033[m'*15)
    else:
        print('\033[36;1m-=-\033[m'*15)
        print('\033[1;31mEscolhe uma opção válida\033[m')
        print('\033[36;1m-=-\033[m'*15)