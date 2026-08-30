import random
import os


def func_1():
    return random.randint(100, 999)


def func_2(a=0, b=0, c=0):
    if a > b:
        aux = a
        a = b
        b = aux

    if a > c:
        aux = a
        a = c
        c = aux

    if b > c:
        aux = b
        b = c
        c = aux

    return a, b, c


def func_3(a=0, b=0, c=0):
    if a == b and b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"


def func_4(celsius=0):
    return (9 / 5) * celsius + 32


def func_5():
    print("==============================")
    print("      PROGRAMA DE FUNÇÕES     ")
    print("==============================")


def func_6():
    print("==============================")
    print("        Até a próxima!        ")
    print("==============================")


def func_7():
    os.system("cls" if os.name == "nt" else "clear")
