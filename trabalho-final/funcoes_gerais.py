# Exibe uma mensagem de boas-vindas ao iniciar o programa.
def inicio_prog():
    """Crie uma função em fng chamada "inicio_prog": deve imprimir na tela uma mensagem de boas-vindas como "Bem vindo <SEU NOME>"."""
    print("===================")
    print("  Bem vindo, Luan  ")
    print("===================")


# Exibe uma mensagem de despedida ao encerrar o programa.
def fim_prog():
    """Crie uma função em fng chamada "fim_prog": deve imprimir uma mensagem de despedida como "Até logo <SEU NOME>"."""
    print("===================")
    print("  Até logo, Luan   ")
    print("===================")


# Calcula o somatório de todos os valores de 0 até x.
def somatorio(x):
    """Crie a função "somatório" no fng, em que receba por parâmetro um valor inteiro qualquer e retorne o somatório de todos os valores até aquele número."""
    # Armazena a soma acumulada.
    soma = 0
    # Percorre todos os números de 0 até x.
    for i in range(x + 1):
        # Soma o valor atual ao acumulador.
        soma += i

    # Retorna o valor total do somatório.
    return soma


# Calcula a média dos valores de 1 até x.
def media_somatorio(x):
    """Crie a função "media_somatorio" no fng, em que receba por parâmetro um valor inteiro qualquer e retorne a média de todos os valores até aquele número."""
    # Se x for 0, retorna 0 para evitar divisão por zero.
    if x == 0:
        return 0

    # Reaproveita a função de somatório para obter a soma total.
    soma = somatorio(x)
    # Divide a soma pela quantidade de números considerada.
    media = soma / x

    # Retorna a média calculada.
    return media


# Realiza operações matemáticas básicas com dois números.
def operacoes_mat(x, y):
    """Crie uma função "operacoes_mat" no fng que receba dois valores por parâmetro e retorne a soma, a subtração, a multiplicação e a divisão inteira e resto da divisão."""
    # Calcula a soma dos dois valores.
    soma = x + y
    # Calcula a subtração do primeiro pelo segundo valor.
    subtracao = x - y
    # Calcula a multiplicação dos dois valores.
    multiplicacao = x * y
    # Calcula a divisão dos dois valores.
    divisao = x / y
    # Calcula o resto da divisão.
    resto = x % y

    # Retorna todos os resultados calculados.
    return soma, subtracao, multiplicacao, divisao, resto
