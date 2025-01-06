Fibonacci = [0,1]
num = 0
n = 1
sequência = [0]
while n != 0:
    n = int(input('\033[mQueres ver qunatso termos da sequência? \033[32m'))
    for e in range(1,n):
        num += Fibonacci[0]
        Fibonacci[0] = num
        sequência.append(num)
        num += Fibonacci[1]
        Fibonacci[1] = num
        sequência.append(num)

        #num = Fibonacci[0] + Fibonacci[1]
        #Fibonacci[0] = Fibonacci[1]
        #Fibonacci[1] = num
        #sequência.append(num)
        
    for e in range(0,n):
        print(sequência[e],end='; ')
    print('\n\033[m')