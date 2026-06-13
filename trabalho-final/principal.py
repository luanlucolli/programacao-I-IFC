import funcoes_gerais as fng
import funcoes_especificas as fne
from funcoes_super_legais_do_trabalho_final import (
    limpar_tela_desse_programa_super_legal as limpar,
)


def menu():

    op = ""

    while op != "0" and op != "S" and op != "s":

        print("Opções:")
        print("S ou 0 - Sair")
        print("M ou 1 - Dias")
        print("E ou 2 - Expressões Matemáticas")
        print("F ou 3 - F0, F1, F2 ou F3")
        print("A ou 4 - Somatório e Média")
        print("P ou 5 - Par ou Ìmpar")
        print("X ou 6 - Operações Matemáticas")

        op = input("Escolha uma das opções: ")

        match op:
            case "S" | "s" | "0":
                fng.fim_prog()
            case "M" | "m" | "1":
                x = int(input("Informe um número de 1 a 7: "))
                print(fne.retorna_dias(x))
            case "E" | "e" | "2":
                fne.expressoes_fn()
            case "F" | "f" | "3":
                x = int(input("Informe um número: "))
                print(fne.numero_N(x))
            case "A" | "a" | "4":
                x = int(input("Informe um número: "))
                print(fng.somatorio(x))
                print(fng.media_somatorio(x))
            case "P" | "p" | "5":
                x = int(input("Informe um número: "))
                if fne.par_impar(x):
                    print("Par")
                else:
                    print("Ímpar")
            case "X" | "x" | "6":
                x = input("Primeiro número:")
                y = input("Segundo número: ")
                soma, subtracao, multiplicacao, divisao, resto, ok = fng.operacoes_mat(
                    x, y
                )
                if ok:
                    print("Soma:", soma)
                    print("Subtração:", subtracao)
                    print("Multiplicação:", multiplicacao)
                    print("Divisão:", divisao)
                    print("Resto:", resto)
                else:
                    print("Valores inválidos ou operações inválida.")
        limpar()


# Função principal
def main():
    fng.inicio_prog()
    menu()


main()
