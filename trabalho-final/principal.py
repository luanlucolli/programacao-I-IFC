# Importa as funções gerais com o apelido fng.
import funcoes_gerais as fng

# Importa as funções específicas com o apelido fne.
import funcoes_especificas as fne

# Importa a função de limpar tela com o apelido limpar.
from funcoes_super_legais_do_trabalho_final import (
    limpar_tela_desse_programa_super_legal as limpar,
)


# Exibe o menu principal e executa a opção escolhida pelo usuário.
def menu():

    # Guarda a opção digitada pelo usuário.
    op = ""

    # Repete o menu até o usuário escolher sair.
    while op != "0" and op != "S" and op != "s":

        # Mostra as opções disponíveis.
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

        # Verifica qual opção foi escolhida.
        match op:
            case "S" | "s" | "0":
                # Encerra o programa com a mensagem de despedida.
                fng.fim_prog()

            case "M" | "m" | "1":
                try:
                    # Lê o número que representa o dia da semana.
                    numero_dia = int(input("Informe um número de 1 a 7: "))
                except:
                    # Informa erro caso o valor digitado não seja numérico.
                    print("Erro: Valores inválidos (letras)")
                else:
                    # Guarda e mostra o dia correspondente ao número informado.
                    dia_semana = fne.retorna_dia_semana(numero_dia)
                    print(dia_semana)

            case "E" | "e" | "2":
                # Exibe as expressões matemáticas e seus resultados.
                fne.expressoes_fn()

            case "F" | "f" | "3":
                try:
                    # Lê o número que será classificado em F0, F1, F2 ou F3.
                    numero = int(input("Informe um número: "))
                except:
                    # Informa erro caso o valor digitado não seja numérico.
                    print("Erro: Valores inválidos (letras)")
                else:
                    # Guarda e mostra a faixa correspondente ao número informado.
                    faixa = fne.numero_N(numero)
                    print(faixa)

            case "A" | "a" | "4":
                try:
                    # Lê o número usado no cálculo do somatório e da média.
                    numero = int(input("Informe um número: "))
                except:
                    # Informa erro caso o valor digitado não seja numérico.
                    print("Erro: Valores inválidos (letras)")
                else:
                    # Calcula o somatório dos números até o valor informado.
                    somatorio = fng.somatorio(numero)
                    # Calcula a média do somatório até o valor informado.
                    media = fng.media_somatorio(numero)

                    # Mostra os resultados calculados.
                    print("Somatório:", somatorio)
                    print("Média:", media)

            case "P" | "p" | "5":
                try:
                    # Lê o número que será verificado como par ou ímpar.
                    numero = int(input("Informe um número: "))
                except:
                    # Informa erro caso o valor digitado não seja numérico.
                    print("Erro: Valores inválidos (letras)")
                else:
                    # Guarda o resultado booleano da verificação.
                    par = fne.par_impar(numero)

                    # Mostra na tela se o número é par ou ímpar.
                    if par:
                        print("Par")
                    else:
                        print("Ímpar")

            case "X" | "x" | "6":
                try:
                    # Lê o primeiro valor da operação matemática.
                    primeiro_numero = int(input("Primeiro número: "))
                    # Lê o segundo valor da operação matemática.
                    segundo_numero = int(input("Segundo número: "))
                except:
                    # Informa erro caso algum dos valores digitados não seja numérico.
                    print("Erro: Valores inválidos (letras)")
                else:
                    # Evita a divisão por zero antes de chamar a função.
                    if segundo_numero == 0:
                        print("Erro: divisão por 0")
                    else:
                        # Recebe os resultados das operações matemáticas.
                        soma, subtracao, multiplicacao, divisao, resto = (
                            fng.operacoes_mat(primeiro_numero, segundo_numero)
                        )
                        # Mostra os resultados na tela.
                        print("Soma:", soma)
                        print("Subtração:", subtracao)
                        print("Multiplicação:", multiplicacao)
                        print("Divisão:", divisao)
                        print("Resto:", resto)
            case _:
                # Informa quando a opção digitada não existe no menu.
                print("Opção inválida.")
        print("")
        # Aguarda o usuário e limpa a tela antes de mostrar o menu novamente.
        limpar()


# Função principal que inicia o programa.
def main():
    # Mostra a mensagem inicial.
    fng.inicio_prog()
    # Chama o menu principal.
    menu()


# Executa o programa.
main()
