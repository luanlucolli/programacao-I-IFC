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

    media = soma/x

    return media
