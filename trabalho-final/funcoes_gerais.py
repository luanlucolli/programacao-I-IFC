def inicio_prog():
    print("===================")
    print("  Bem vindo, Luan  ")
    print("===================")


def fim_prog():
    print("===================")
    print("  Até logo, Luan   ")
    print("===================")


def somatorio(x):
    soma = 0
    for i in range(x + 1):
        soma += i

    return soma


def media_somatorio(x):
    if x == 0:
        return 0

    soma = somatorio(x)
    media = soma / x

    return media


def operacoes_mat(x, y):
    soma = x + y
    subtracao = x - y
    multiplicacao = x * y
    divisao = x // y
    resto = x % y

    return soma, subtracao, multiplicacao, divisao, resto
