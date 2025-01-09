num = 0
while True:
    num = int(input('\033[mQueres ver a tabuada de que número? \033[1;33m'))
    if num < 0:        
        break
    print('\033[m-'*20)
    for e in range(1,13):
        print(f'{e:2} * {num:2} = {e*num:2}')
    print('\033[m-'*20)
print('\033[mPrograma tabuada terminado')