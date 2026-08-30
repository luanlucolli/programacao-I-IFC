'''Crie um programa principal e um arquivo de funções. Ao invés de importar o arquivo de funções no programa principal, importe cada uma das funções individualmente (dando apelido a cada uma). No programa principal, fala um menu com as seguintes opções:

0 - Sair
1  - Ordem de Valores
2 - Triângulo
3 - Fahrenheit
No script de funções, crie as seguintes funções:

 função que deve retornar um número aleatório entre 100 e 999.
função que receba de três valores, e que retorne em ordem crescente estes mesmos três argumentos.
função que recebe por parametro as três medidas de um triângulo. Deverá retornar uma stringe de texto  considerando as três medidas do triângulo: se forem iguais = equilátero, duas medidas iguais = isóceles, e três diferentes = escaleno).
função que recebe por parametro um valor de temperatura em graus Celsius e retorna a converção para graus Fahrenheit. Lembrando que: F = (9/5) * C + 32
função que imprime um cabeçalho na tela (use a criatividade)
função que imprime um rodapé na tela (novamente, use a criatividade)
função que limpa a tela do terminal.
Ao digitar a opção 1, deverão ser gerados 3 valores aleatórios (biblioteca random) e passados para a função devida. O retorno da função deve ser impresso na tela. 
Ao digital a opção 2, deve ser solicitado ao usuário três valores que correspondem as medidas de um triângulo. Posteriormente, imprimir na tela a classificação desse triângulo.
Ao digitar 3, deverá solicitar ao usuário um valor de temperatura em ºC e após imprimir na tela a conversão em ºF.
Imprima (uma única vez) o cabeçalho ao entrar no programa e o rodapé ao sair.
- Não esqueça de usar o try, except e else sempre que necessário.
- não esqueça os valores padrão nas funções.
- não esqueça de limpar a tela sempre que possível.'''

from funcs import func_1 as aleatorio
from funcs import func_2 as ordem_valores
from funcs import func_3 as tipo_triangulo
from funcs import func_4 as fahrenheit
from funcs import func_5 as cabecalho
from funcs import func_6 as rodape
from funcs import func_7 as limpar


# Mostra o cabeçalho uma única vez ao iniciar o programa.
cabecalho()
print("")

# Guarda a opção digitada pelo usuário.
op = ""

# Repete o menu até o usuário escolher sair.
while op != "0":

    # Mostra as opções disponíveis.
    print("Opções:")
    print("0 - Sair")
    print("1 - Ordem de Valores")
    print("2 - Triângulo")
    print("3 - Fahrenheit")

    # Lê a opção desejada.
    op = input("Escolha uma das opções: ")
    print("")

    match op:
        case "0":
            rodape()

        case "1":
            numero_1 = aleatorio()
            numero_2 = aleatorio()
            numero_3 = aleatorio()

            primeiro, segundo, terceiro = ordem_valores(
                numero_1, numero_2, numero_3
            )

            print("Valores gerados:", numero_1, numero_2, numero_3)
            print("Em ordem crescente:", primeiro, segundo, terceiro)

        case "2":
            try:
                medida_1 = float(input("Informe a primeira medida: "))
                medida_2 = float(input("Informe a segunda medida: "))
                medida_3 = float(input("Informe a terceira medida: "))
            except:
                print("Valor inválido. Informe números.")
            else:
                tipo = tipo_triangulo(medida_1, medida_2, medida_3)
                print("O triângulo é", tipo + ".")

        case "3":
            try:
                temperatura = float(input("Informe a temperatura em ºC: "))
            except:
                print("Valor inválido. Informe um número.")
            else:
                resultado = fahrenheit(temperatura)
                print("Temperatura em ºF:", resultado)

        case _:
            print("Opção inválida.")

    if op != "0":
        print("")
        input("Pressione Enter para continuar...")
        limpar()
