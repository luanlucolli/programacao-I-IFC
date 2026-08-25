"""2 - Faça um programa que solicite ao usuário um valor inteiro (verifique
com try, except). Faça uma função que imprima se este valor é par ou ímpar e
outra função que imprima se ele é positivo, negativo ou zero."""


def par_impar(n=0):
    if n % 2 == 0:
        print("Par")
    else:
        print("Ímpar")


def positivo_negativo(n=0):
    if n > 0:
        print("Positivo")
    elif n < 0:
        print("Negativo")
    else:
        print("Zero")


try:
    n = int(input("numero inteiro: "))
except:
    print("Valor inválido")
else:
    par_impar(n)
    positivo_negativo(n)
