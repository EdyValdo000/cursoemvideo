# 912.00 kz -> 1.00 US
money = float(input('Quato dinheiro tens? '))
refDol = 1.00
refKz = 912.00
dol = (money * refDol) / refKz
print('Com \033[1;31m{}\033[m\033[1;32mkz\033[m tu podes comprar \033[1;36m{:.2f}\033[m\033[1;32mUS\033[m'.format(money,dol))