text = str(input('Digita um texto: ')).upper()
busca = 'A'
print('O teu texto tem \033[1;36m{}\033[m caracteres \033[1;36m{}\033[m'.format(text.count(busca),busca))
print('O caracter \033[1;36m{}\033[m aparece a 1ª vez na posição \033[1;36m{}\033[m'.format(busca,text.find(busca)))
print('O caracter \033[1;36m{}\033[m aparece a última vez na posição \033[1;36m{}\033[m'.format(busca,text.rfind(busca)))