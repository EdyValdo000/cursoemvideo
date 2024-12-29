number1 = int(input('Digite o 1º número: '))
number2 = int(input('Digite o 2º número: '))
number3 = int(input('Digite o 3º número: '))
numbers = [number1, number2, number3]
Max = max(numbers)
Min = min(numbers)
print('O menor número é {} e o maior é {}'.format(Min,Max))