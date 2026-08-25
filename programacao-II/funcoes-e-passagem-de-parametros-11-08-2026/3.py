'''3 - Faça um programa que solicite dois valores ao usuário (verifique com
try, except). Faça funções que imprimam o resultado da adição, subtração,
multiplicação, divisão inteira, divisão fracionária, resto da divisão e
exponenciação. O programa deve parar se os dois números forem iguais a zero.'''


def soma(n1=0, n2=0):
    print(f"Soma: {n1 + n2}")


def subtracao(n1=0, n2=0):
    print(f"Subtração: {n1 - n2}")


def multiplicacao(n1=0, n2=0):
    print(f"Multiplicação: {n1 * n2}")


def divisao_inteira(n1=0, n2=0):
    if n2 == 0:
        print("Divisão inteira: não é possível dividir por zero")
    else:
        print(f"Divisão inteira: {n1 // n2}")


def divisao_fracionaria(n1=0, n2=0):
    if n2 == 0:
        print("Divisão fracionária: não é possível dividir por zero")
    else:
        print(f"Divisão fracionária: {n1 / n2}")


def resto_divisao(n1=0, n2=0):
    if n2 == 0:
        print("Resto da divisão: não é possível dividir por zero")
    else:
        print(f"Resto da divisão: {n1 % n2}")


def exponenciacao(n1=0, n2=0):
    print(f"Exponenciação: {n1 ** n2}")


while True:
    try:
        n1 = int(input("insira um número: "))
        n2 = int(input("insira um número: "))
    except:
        print("valor inválido")
        continue

    if n1 == 0 and n2 == 0:
        break

    soma(n1, n2)
    subtracao(n1, n2)
    multiplicacao(n1, n2)
    divisao_inteira(n1, n2)
    divisao_fracionaria(n1, n2)
    resto_divisao(n1, n2)
    exponenciacao(n1, n2)
