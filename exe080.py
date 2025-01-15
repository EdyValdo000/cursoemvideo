números = list()
númerosOrganizados = list()
elemento = 0
for c in range(0,5):    
    números.append(int(input('Digite um número: ')))
while True:    
    if len(númerosOrganizados) == 5:
        break
    elemento = min(números)
    númerosOrganizados.append(elemento)
    del números[números.index(elemento)]
print(f'Os valores ordenados são {númerosOrganizados}')