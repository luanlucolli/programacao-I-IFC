def listar_numeros_ate_for():
    numero = int(input("insira um número: "))

    for i in range(numero + 1):
        print(i)


def listar_pares_ate_for():
    numero = int(input("insira um número: "))

    for i in range(numero + 1):
        if i % 2 == 0:
            print(i)


def listar_impares_ate_1000_for():
    for i in range(1, 1001, 3):
        if i % 2 != 0:
            print(i)

        if i + 2 <= 1000 and (i + 2) % 2 != 0:
            print(i + 2)


def multiplicar_por_somatoria_for():
    numero1 = int(input("primeiro número: "))
    numero2 = int(input("segundo número: "))

    resultado = 0

    for i in range(numero1):
        resultado += numero2

    print("resultado:", resultado)


def calcular_soma_media_intervalo_for():
    soma = 0
    quantidade = 0

    for i in range(223, 446):
        soma += i
        quantidade += 1

    media = soma / quantidade

    print("soma:", soma)
    print("média:", media)


def listar_numeros_ate_while():
    numero = int(input("insira um número: "))
    i = 0

    while i <= numero:
        print(i)
        i += 1


def listar_pares_ate_while():
    numero = int(input("insira um número: "))
    i = 0

    while i <= numero:
        if i % 2 == 0:
            print(i)
        i += 1


def listar_impares_ate_1000_while():
    i = 1

    while i <= 1000:
        if i % 2 != 0:
            print(i)

        if i + 2 <= 1000 and (i + 2) % 2 != 0:
            print(i + 2)

        i += 3


def multiplicar_por_somatoria_while():
    numero1 = int(input("primeiro número: "))
    numero2 = int(input("segundo número: "))
    resultado = 0
    contador = 0

    while contador < numero1:
        resultado += numero2
        contador += 1

    print("resultado:", resultado)


def calcular_soma_media_intervalo_while():
    soma = 0
    quantidade = 0
    numero = 223

    while numero <= 445:
        soma += numero
        quantidade += 1
        numero += 1

    media = soma / quantidade

    print("soma:", soma)
    print("média:", media)
