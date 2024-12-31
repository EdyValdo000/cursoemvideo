number = int(input('Digite um número: '))
if number % 2 == 0:
    print('\033[1;36mO número é par!\033[m')
else:
    print('\033[1;31mO número é impar.\033[m')