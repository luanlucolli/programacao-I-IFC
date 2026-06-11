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
    print("2*5/20 + 30/15*2​ =", 2*5/20 + 30/15*2)
    print("2*(5/20) + 35/(15*2) =", 2*(5/20) + 35/(15*2))
    print("23 mod 4 =", 23%4)
    