houseMoney = float(input('QUal é o valor da casa? '))
Salary = float(input('Qual é o seu salário? '))
yearPayment = int(input('Vais pagar em quantos anos? '))

hosePaymet = houseMoney / (12 * yearPayment)
if Salary * 0.3 <= hosePaymet:
    print('\033[1;31mNão vais poder pagar a casa de {}Kz em {} anos, cada parcela é de {:.2f}Kz'.format(houseMoney,yearPayment,hosePaymet))
    print('Emprestimo negado.\033[m')
else:
    if yearPayment == 1:
        print('\033[1;32mVais poder pagar a casa em {} ano pagando {:.2f} por cada mês'.format(yearPayment,hosePaymet))
        print('Emprestimo aprovado.\033[m')
    else:
        print('\033[1;32mVais poder pagar a casa em {} anos pagando {:.2f} por cada mês'.format(yearPayment,hosePaymet))
        print('Emprestimo aprovado.\033[m')