filme = {
    'nome' : 'Star Waras',
    'ano' : 1994,
    'director' : 'Jorge Lucas'
}

filme.values() #Tudo que está depois dois pontos
filme.keys() #As chaves
filme.items() #Tudo que está dentro do dicionário, da para usar como o enumerate

for k, v in filme.items():
    print(f'{k} - {v}')