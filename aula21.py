# Para entrar no interactiv help podes digitar a função help() no cmd do python ou help(nome da função)
def contagem (inicio, fim, passo):
    """
Descrição da Função contagem
A função contagem(inicio, fim, passo) imprime uma sequência numérica que vai de inicio até fim, incrementando ou decrementando de acordo com o valor de passo.

Funcionamento:
Criação da lista sequência:

Armazena os números da contagem para posterior exibição.
Impressão de uma linha separadora (= repetido 55 vezes).

Correção do valor de passo caso seja zero:

Se passo == 0, ele é alterado para 1 para evitar um loop infinito.
Impressão do cabeçalho da contagem, informando os valores de início, fim e passo (sempre positivos para melhor compreensão).

Definição da lógica da contagem:

Se inicio < fim:
A contagem é crescente, então range(inicio, fim+1, passo).
Se inicio > fim:
A contagem é decrescente, então range(inicio, fim-1, abs(passo)*-1), garantindo que o passo seja negativo.
Exibição da sequência de números:

Utiliza enumerate() para formatar a saída de forma que os números sejam separados por vírgulas, exceto o último, que termina com um ponto final (.).
    """    
    #------------------------------------------------
    # Para usar uma variável global dentro de uma função tens de colocar 
    global valor
    valor = 15
    #------------------------------------------------
    sequência = list()
    print(f'='*55)
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {abs(fim)} de {abs(passo)} em {abs(passo)}')
    if inicio < fim:
        for valor in range(inicio, fim+1, passo):
           sequência.append(valor) 
    elif fim < inicio:
        for valor in range(inicio, fim-1, abs(passo)*-1):
            sequência.append(valor)
    for index, valor in enumerate(sequência):
        print(f'{valor}',end=', ' if index != len(sequência)-1 else '.\n')
    print(f'='*55)

help(contagem)

# Os parâmetros opcionais é a mesma coisa que em C#, vc inicializa a variável dentro da criação da função
valor = 0
