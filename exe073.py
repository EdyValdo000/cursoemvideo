selecoes_top_20 = (
    "Brasil",
    "Argentina",
    "França",
    "Bélgica",
    "Inglaterra",
    "Portugal",
    "Espanha",
    "Itália",
    "Países Baixos",
    "Croácia",
    "Marrocos",
    "Alemanha",
    "Suíça",
    "Uruguai",
    "Estados Unidos",
    "Colômbia",
    "Senegal",
    "Japão",
    "Dinamarca",
    "México"
)

print(f'Os 5 primeiros colocados são {selecoes_top_20[:5]}')
print(f'Os 4 ultimos colocados são {selecoes_top_20[-4:]}')
print(f'Os times em orde alfabetica {sorted(selecoes_top_20)}.')
print(f'Marrocos está na {selecoes_top_20.index('Marrocos') + 1}ª posição')