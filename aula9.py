frase = 'Edivaldo Coelho'
print(frase.lower())
len(frase) #tamanho da string
frase.count('o') #conta o caracter que está na string
frase.find('do') #retorna a posição que começa o texto que passei como parametro
'Coelho' in frase #Retorna True ou False
frase.replace('Edivaldo','Edy Valdo') #É o mesmo que me C#
frase.upper() #Coloca a string tota maiuscula
frase.lower() #coloca tudo para minusculo
frase.capitalize() #1º caracter maiusculo e o resto minusculo
frase.title() #Ele faz o captalize por cada espaço entre as palavras
frase.strip() #Apaga os espaços no início e no fim da string
frase.rstrip() #Apaga os espaços da direita da string
frase.lstrip() #Apaga os espaços da esquerda da string
frase.split() #Separa por padrão com o espaço
' '.join(frase) #Juta a lista separanso os elementos por ' '