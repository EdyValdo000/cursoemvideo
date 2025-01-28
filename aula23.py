try:
    a = int(input('Númerador: '))
    b = int(input('Denominador: '))
    c = a/b
except (ValueError, TypeError):
    print(f'Deu erro nos valores passados')
except ZeroDivisionError:
    print('Não da para dividir por zero')
except Exception as erro:
    print(f'Deu erro na classe {erro.__class__}')
else:
    print(f'Deu certo e o resultado é {c}')
finally:
    print(f'Volte sempre.')