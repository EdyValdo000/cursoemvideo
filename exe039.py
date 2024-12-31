from datetime import date
year = int(input('Nasceste em que ano? '))
dateToday = date.today()
yearsOld = dateToday.year - year

if yearsOld < 18:
    print('Ainda não tens de te alistar para o recenciamento militar, faltam \033[1;32m{}\033[m anos.'.format(18-yearsOld))
elif yearsOld == 18:
    print('Tens de te alistar no recenciamento militar, já tens \033[1;33m{}\033[m anos.'.format(yearsOld))
elif yearsOld > 18:
    print('Passaste \033[1;31m{}\033[m anos para se te inscreveres no recenciamento militar.'.format(yearsOld - 18))