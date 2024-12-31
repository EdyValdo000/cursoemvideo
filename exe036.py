houseMoney = float(input('QUal é o valor da casa? '))
Salary = float(input('Qual é o seu salário? '))
yearPayment = int(input('Vais pagar em quantos anos? '))

hosePaymet = houseMoney / (12 * yearPayment)
if Salary * 0.3 < hosePaymet:
    print('\033[1;31mNão vais poder pagar a casa de {}Kz em {} anos, cada parcela é de {:.2f}Kz\033[m'.format(houseMoney,yearPayment,hosePaymet))
else:
    if yearPayment == 1:
        print('\033[1;32mVais poder pagar a casa em {:.2f} ano pagando {:.2f} por cada mês\033[m'.format(yearPayment,hosePaymet))
    else:
        print('\033[1;32mVais poder pagar a casa em {:.2f} anos pagando {:.2f} por cada mês\033[m'.format(yearPayment,hosePaymet))