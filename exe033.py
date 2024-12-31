number1 = int(input('\033[1;33mDigite o 1º número: '))
number2 = int(input('Digite o 2º número: '))
number3 = int(input('Digite o 3º número: '))
numbers = [number1, number2, number3]
Max = max(numbers)
Min = min(numbers)
print('\033[mO menor número é \033[1;31m{}\033[m e o maior é \033[1;32m{}\033[m'.format(Min,Max))