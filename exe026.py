text = input('Digita um texto: ')
busca = 'A'
print('O teu texto tem {} caracteres {}'.format(text.count(busca),busca))
print('O caracter {} aparece a 1ª vez na posição {}'.format(busca,text.find(busca)))
print('O caracter {} aparece a última vez na posição {}'.format(busca,text.rfind(busca)))