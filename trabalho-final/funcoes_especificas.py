def retorna_dias(diaDaSemana):
    match diaDaSemana:
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
            return "Entrada inválida"


def expressoes_fn():
    print("Raiz de 195 =", 195 ** (0.5))
    print("2*5/20 + 30/15*2​ =", 2 * 5 / 20 + 30 / 15 * 2)
    print("2*(5/20) + 35/(15*2) =", 2 * (5 / 20) + 35 / (15 * 2))
    print("23 mod 4 =", 23 % 4)


def numero_N(x):
    if x <= 0:
        return "F0"
    elif x <= 10:
        return "F1"
    elif x <= 100:
        return "F2"
    else:
        return "F3"


def par_impar(x):
    return x % 2 == 0

    """
     try:
        n1 = int(input("n1: "))
        n2 = int(input("n2: "))
    except:
        print("valores inválidos\n")
    else:
        print("subtração:",n1-n2)
    """
