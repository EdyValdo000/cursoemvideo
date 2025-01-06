e = 1
factorial = 1
num = int(input('Digite um número: '))
while num+1 > e:
    factorial *= (e)
    e += 1
print('{}! = {}'.format(num,factorial))