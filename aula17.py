lista = ['Banana', 12, 'feijão', 5.23]
lista.insert(0,14) # Iserre na posição
lista.pop(3) # Elimina o que está na posição 3, se o parametro for nulo elimina o último elemento
del lista[3] # Faz isso que estás a ler
lista.remove('Banana') # Retira da lista o valor de parametro

novaLista = list(range(3,13)) #Cria uma lista com os valores de 3 até 14.
#novaLista.sort() #Organiza por ordem
novaLista.sort(reverse=True)

print(novaLista) #Inverso

for c, v in enumerate(novaLista):
    print(f'..... {c} .....{v}') #Apresenta a posição e o valor da lista