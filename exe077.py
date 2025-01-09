palavras = (
    "cafe",
    "Luz",
    "CDC",
    "camelo",
    "banana",
    "sabado",
    "mamae",
    "voce",
    "irmao",
    "feliz",
    "acao",
    "coracao",
    "passaro",
    "maracuja",
    "limao",
    "linguica",
    "pincel",
    "tatu",
    "amarelo",
    "azul",
    "computador",
    "livro"
)
contador = númeroDeVogais = 0
while contador < len(palavras):
    
    for e in range(0,len(palavras[contador])):
        if 'a' == palavras[contador][e]:
            númeroDeVogais += 1
        if 'e' == palavras[contador][e]:
            númeroDeVogais += 1
        if 'i' == palavras[contador][e]:
            númeroDeVogais += 1 
        if 'o' == palavras[contador][e]:
            númeroDeVogais += 1 
        if 'u' == palavras[contador][e]:
            númeroDeVogais += 1 

    if númeroDeVogais == 0:
        print(f'A palavra \033[33;1m{palavras[contador]}\033[m não tem vogais: ',end='')    
    elif númeroDeVogais == 1:
        print(f'A palavra \033[33;1m{palavras[contador]}\033[m tem a seginte vogal: ',end='')
    else:
        print(f'A palavra \033[33;1m{palavras[contador]}\033[m tem as segintes vogais: ',end='')
    
    númeroDeVogais = 0

    for e in range(0,len(palavras[contador])):
        if 'a' == palavras[contador][e]:
            print('a', end=' ') 
        if 'e' == palavras[contador][e]:
            print('e', end=' ')
        if 'i' == palavras[contador][e]:
            print('i', end=' ') 
        if 'o' == palavras[contador][e]:
            print('o', end=' ') 
        if 'u' == palavras[contador][e]:
            print('u', end=' ') 
    print('')
    contador += 1