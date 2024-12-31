from datetime import date
dateToday = date.today()
year = int(input('Digite sua data de nascimento para saber a sua categoria: '))

yearsOld = dateToday.year - year

print('A sua categoria é',end=' ')
if yearsOld <= 9:
    print('\033[1;36mMIRIN\033[m',end=' ')
elif 9 < yearsOld <= 14:
    print('\033[1;36mINFANTIL\033[m',end=' ')
elif 14 < yearsOld <= 19:
    print('\033[1;32mJUNIOR\033[m',end=' ')
elif yearsOld == 20:
    print('\033[1;33mSENIOR\033[m',end=' ')
elif yearsOld > 20:
    print('\033[1;41mMASTER\033[m',end=' ')

print('com \033[1;35m{}\033[m anos'.format(yearsOld))