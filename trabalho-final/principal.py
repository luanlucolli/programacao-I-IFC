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
                try:
                    x = int(input("Informe um número de 1 a 7: "))
                except:
                    print("Entrada Inválida")
                else:
                    print(fne.retorna_dias(x))

            case "E" | "e" | "2":
                fne.expressoes_fn()

            case "F" | "f" | "3":
                try:
                    x = int(input("Informe um número: "))
                except:
                    print("Erro: Valores inválidos (letras)")
                else:
                    print(fne.numero_N(x))

            case "A" | "a" | "4":
                try:
                    x = int(input("Informe um número: "))
                except:
                    print("Erro: Valores inválidos (letras)")
                else:
                    somatorio = fng.somatorio(x)
                    media = fng.media_somatorio(x)

                    print("Somatório:", somatorio)
                    print("Média:", media)

            case "P" | "p" | "5":
                try:
                    x = int(input("Informe um número: "))
                except:
                    print("Erro: Valores inválidos (letras)")
                else:
                    if fne.par_impar(x):
                        print("Par")
                    else:
                        print("Ímpar")

            case "X" | "x" | "6":
                try:
                    x = int(input("Primeiro número: "))
                    y = int(input("Segundo número: "))
                except:
                    print("Erro: Valores inválidos (letras)")
                else:
                    if y == 0:
                        print("Erro: divisão por 0")
                    else:
                        soma, subtracao, multiplicacao, divisao, resto = (
                            fng.operacoes_mat(x, y)
                        )
                        print("Soma:", soma)
                        print("Subtração:", subtracao)
                        print("Multiplicação:", multiplicacao)
                        print("Divisão:", divisao)
                        print("Resto:", resto)
        limpar()


# Função principal
def main():
    fng.inicio_prog()
    menu()


main()
