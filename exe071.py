#200; 500; 1000; 2000; 5000;
money = int(input('Digite o valor que quer sacar (Kz): '))
total = money
valorDasNotas = [50, 20, 10, 1]
númeroDeNotas = [0, 0, 0, 0]
while True:
    if money // valorDasNotas[0] != 0:
        númeroDeNotas[0] = money // valorDasNotas[0]
        money -= númeroDeNotas[0] * valorDasNotas[0]
    
    elif money // valorDasNotas[1] != 0:
        númeroDeNotas[1] = money // valorDasNotas[1]
        money -= númeroDeNotas[1] * valorDasNotas[1]
    
    elif money // valorDasNotas[2] != 0:
        númeroDeNotas[2] = money // valorDasNotas[2]
        money -= númeroDeNotas[2] * valorDasNotas[2]

    elif money // valorDasNotas[3] != 0:
        númeroDeNotas[3] = money // valorDasNotas[3]
        money -= númeroDeNotas[3] * valorDasNotas[3]

    if money == 0:
        break

print(f'Para sacares {total}Kz')
for e in range(0,len(valorDasNotas)):
    if númeroDeNotas[e] > 0:
        print(f'Tu vais usar {númeroDeNotas[e]} notas de {valorDasNotas[e]}Kz ')
print('\nFIM')