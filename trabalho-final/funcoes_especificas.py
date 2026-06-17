# Retorna o nome do dia da semana de acordo com o número informado.
def retorna_dia_semana(x):
    """Crie uma função chamada "retorna_meses" em fne, que receberá um número de 1 a 7 e retorna o nome do dia da semana por extenso. Caso o valor não corresponda a algum dia, deverá ser retornado "Entrada Inválida"."""
    # Verifica qual dia corresponde ao número recebido.
    match x:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda-Feira"
        case 3:
            return "Terça-Feira"
        case 4:
            return "Quarta-Feira"
        case 5:
            return "Quinta-Feira"
        case 6:
            return "Sexta-Feira"
        case 7:
            return "Sábado"
        case _:
            return "Entrada Inválida"


# Exibe as expressões matemáticas solicitadas no trabalho e seus resultados.
def expressoes_fn():
    """Crie uma função "expressoes_fn" em fne que calcule e exiba a equação e também o valor da resposta de cada expressão pedida no trabalho."""
    print("Raiz de 195 =", 195 ** (0.5))
    print("2*5/20 + 30/15*2​ =", 2 * 5 / 20 + 30 / 15 * 2)
    print("2*(5/20) + 35/(15*2) =", 2 * (5 / 20) + 35 / (15 * 2))
    print("23 mod 4 =", 23 % 4)


# Classifica o número recebido em F0, F1, F2 ou F3.
def numero_N(x):
    """Crie uma função "numero_N" no fne que deverá receber por parâmetro um número N e retorne "F0", "F1", "F2" ou "F3", conforme a condição do enunciado."""
    # Retorna F0 se o número for menor ou igual a zero.
    if x <= 0:
        return "F0"
    # Retorna F1 se o número estiver entre 1 e 10.
    elif x <= 10:
        return "F1"
    # Retorna F2 se o número estiver entre 11 e 100.
    elif x <= 100:
        return "F2"
    # Retorna F3 se o número for maior que 100.
    else:
        return "F3"


# Retorna True se o número for par e False se for ímpar.
def par_impar(x):
    """Crie uma função "par_impar" no fne que receba um valor por parâmetro e retorne True ou False, dependendo se o número é par ou ímpar."""
    return x % 2 == 0
