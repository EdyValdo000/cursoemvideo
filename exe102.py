def factorial (número, show=False):
    """
    número é o valor que queres saber o factorial
    show é uma variavel para escolheres se queres ver todos os números envolvidos no calculo do factorial de um número
    """
    resultado = 1
    resposta = f'O factorial de {número} é... \n'
    for c in range(número, 0, -1):
        resultado *= c
    if not show:
        resposta += f'{número}! = '+str(resultado)
        print(resposta)
    else:
        for valor in range(número,0,-1):
            resposta += (str(valor) + (' X ' if valor != 1 else ''))
        print(resposta,end=f' = {resultado}\n')

factorial(5,True)
