# 912.00 kz -> 1.00 US
money = float(input('Quato dinheiro tens? '))
refDol = 1.00
refKz = 912.00
dol = (money * refDol) / refKz
print('Com {}kz tu podes comprar {:.2f}US'.format(money,dol))