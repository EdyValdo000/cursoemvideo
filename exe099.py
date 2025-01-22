def maior(*números):
    if len(números):
        mensagem = 'Os valores passados forram '
        mensagemMaiorValor = f'O maior valor é {max(números)}'

        for index, valor in enumerate(números):
            mensagem += str(valor)
            mensagem += ', ' if index!=len(números)-1 else '.'
        
        print(f'='*(len(mensagem)+2))
        print(f'{mensagem:^{len(mensagem)+2}}')    
        if len(números) != 0:
            print(f'{mensagemMaiorValor:^{len(mensagem)+2}}')
        print(f'='*(len(mensagem)+2))

    else:
        semValores = 'Não informaste valores'
        print(f'='*(len(semValores)+2))
        print(f'{semValores:^{len(semValores)+2}}')    
        print(f'='*(len(semValores)+2))


maior()
maior(0,1,5)
maior(2,67,1290)
