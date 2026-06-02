'''Faça um programa que apresente um menu ao usuário que deverá fornecer opções de operações matemáticas: 1 - somar, 2 - subtrair, etc. A letra "s" encerra o programa. O menu deverá tratar entradas inválidas. 
O programa também deverá perguntar dois valores numéricos ao usuário, que serão convertidos e passados por parâmetros nas funções. Logo, as entradas de usuário deverão ser verificadas se são números válidos.

O programa deve ter 5 funções (não métodos), um para cada operação matemática: adição, subtração, multiplicação, divisão e resto de divisão.

Cada uma das funções deverá receber por parâmetro dois números e executar as devidas operações matemáticas e retornar o resultado.
'''

import math as math

op = ""



while op != 's' and op != 'S':
    print("1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n5 - resto\n6 - exponenciação\n7 - raiz quadrada\ns ou S - sair")
    op = input("opção: ")
    
    match op:
        case "1":
            math.soma()
        case "2":
            math.subtracao()
        case "3":
            math.multiplicacao()
        case "4":
            math.divisao()
        case "5":
            math.resto()
        case "6":
            math.exponenciacao()
        case "7":
            math.raizQuadrada()
        case "8":
            math.somatorio()
        case "s" | "S":
            print("vlw flw")
        case _:
            print("opção inválida")
            
    print("")
    
    
