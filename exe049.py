num = int(input('Qual é o número que vais usar para a tabuada? '))
print('\033[1;33m-=-\033[m'*5)
for e in range(1,13):
    print('\033[1;32m{:^2} * {:^2} = {:^2}\033[m'.format(num,e,e*num))
print('\033[1;33m-=-\033[m'*5)