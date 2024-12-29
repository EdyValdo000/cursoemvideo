"""Divida o número do ano por 4.
Se não for divisível, não é bissexto.
Se for divisível por 4, veja se também é divisível por 100.
Se não for divisível por 100, é bissexto.
Se for divisível por 100, veja se também é divisível por 400.
Se for, é bissexto.
Caso contrário, não é bissexto."""
year = int(input('Digite o ano: '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('O ano é bissexto.')
        else:
            print('O ano não é bissexto.')
    else:
        print('O ano é bissexto.')
else:
    print('O ano não é bissexto.')