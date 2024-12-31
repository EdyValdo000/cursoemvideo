"""Divida o número do ano por 4.
Se não for divisível, não é bissexto.
Se for divisível por 4, veja se também é divisível por 100.
Se não for divisível por 100, é bissexto.
Se for divisível por 100, veja se também é divisível por 400.
Se for, é bissexto.
Caso contrário, não é bissexto."""
from datetime import date
year = int(input('Digite o ano: '))
if year == 0:
    year = date.today().year
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('O ano {} \033[1;32mé bissexto.\033[m'.format(year))
    else:
        print('O ano {} \033[1;31mnão é bissexto.\033[m'.format(year))
else:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('O ano {} \033[1;32mé bissexto.\033[m'.format(year))
    else:
        print('O ano {} \033[1;31mnão é bissexto.\033[m'.format(year))