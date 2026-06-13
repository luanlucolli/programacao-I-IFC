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
    soma = 0
    for i in range(x + 1):
        soma += i

    media = soma / x

    return media


def operacoes_mat(x, y):
    try:
        x = int(x)
        y = int(y)

        soma = x + y
        subtracao = x - y
        multiplicacao = x * y
        divisao = x / y
        resto = x % y

        return soma, subtracao, multiplicacao, divisao, resto, True

    except:
        return 0, 0, 0, 0, 0, False
