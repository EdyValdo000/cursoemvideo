from datetime import date
print("""
[1] Homem
[2] Mulher""")
sexo = int(input("""DIgite: """))
if sexo == 1:
    year = int(input('Nasceste em que ano? '))
    dateToday = date.today()
    yearsOld = dateToday.year - year
    if yearsOld < 18:
        print('Ainda não tens de te alistar para o recenciamento militar, vais te alistar em \033[1;32m{}\033[m vai ser daqui a \033[1;32m{}\033[m anos.'.format(18 - yearsOld + dateToday.year, 18 - yearsOld))
    elif yearsOld == 18:
        print('Tens de te alistar no recenciamento militar, já tens \033[1;33m{}\033[m anos.'.format(yearsOld))
    elif yearsOld > 18:
        print('O teu alistament para o recenciamento militar foi em \033[1;31m{}\033[m foi a \033[1;31m{}\033[m anos.'.format( dateToday.year - (yearsOld - 18), yearsOld - 18))
elif sexo == 2:
    print('\033[1;35mMulheres não presisão ser alistadas no recenciamneto militar.\033[m')
else:
    print('\033[1;31mEscolhe uma opção valida.\033[m')