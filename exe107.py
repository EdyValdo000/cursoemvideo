import math
nome_da_funcao = 'math'
funcao = getattr(__builtins__, nome_da_funcao)  # Obtém a função print
print(funcao.__doc__)  # Exibe a documentação da função print