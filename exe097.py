def escreva(mensagem):
    tamanho = len(mensagem)
    print('~'* (tamanho + 2))
    print(f'{mensagem:^{tamanho+2}}')
    print('~'* (tamanho + 2))


# Principal
sms = str(input('Mensagem: '))
escreva(sms)
