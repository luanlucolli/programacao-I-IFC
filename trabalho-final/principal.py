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
        print("X ou 6 - Operações Matemáticas\n")

        op = input("Escolha uma das opções: ")
        print("")

        match op:
            case "S" | "s" | "0":
                fng.fim_prog()

            case "M" | "m" | "1":
                try:
                    numero_dia = int(input("Informe um número de 1 a 7: "))
                except:
                    print("Erro: Valores inválidos (letras)")
                else:
                    dia_semana = fne.retorna_dia_semana(numero_dia)
                    print(dia_semana)

            case "E" | "e" | "2":
                fne.expressoes_fn()

            case "F" | "f" | "3":
                try:
                    numero = int(input("Informe um número: "))
                except:
                    print("Erro: Valores inválidos (letras)")
                else:
                    faixa = fne.numero_N(numero)
                    print(faixa)

            case "A" | "a" | "4":
                try:
                    numero = int(input("Informe um número: "))
                except:
                    print("Erro: Valores inválidos (letras)")
                else:
                    somatorio = fng.somatorio(numero)
                    media = fng.media_somatorio(numero)

                    print("Somatório:", somatorio)
                    print("Média:", media)

            case "P" | "p" | "5":
                try:
                    numero = int(input("Informe um número: "))
                except:
                    print("Erro: Valores inválidos (letras)")
                else:
                    par = fne.par_impar(numero)

                    if par:
                        print("Par")
                    else:
                        print("Ímpar")

            case "X" | "x" | "6":
                try:
                    primeiro_numero = int(input("Primeiro número: "))
                    segundo_numero = int(input("Segundo número: "))
                except:
                    print("Erro: Valores inválidos (letras)")
                else:
                    if segundo_numero == 0:
                        print("Erro: divisão por 0")
                    else:
                        soma, subtracao, multiplicacao, divisao, resto = (
                            fng.operacoes_mat(primeiro_numero, segundo_numero)
                        )
                        print("Soma:", soma)
                        print("Subtração:", subtracao)
                        print("Multiplicação:", multiplicacao)
                        print("Divisão:", divisao)
                        print("Resto:", resto)
            case _:
                print("Opção inválida.")
        print("")
        limpar()


# Função principal
def main():
    fng.inicio_prog()
    menu()


main()
