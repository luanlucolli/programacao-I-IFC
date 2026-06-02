minutosPerdidosCigarro = 10

qtdCigarros = int(input("quantidade de cigarros fumados por dia: "))
anosFumando = int(input("quantos anos fumando: "))

totalMinutosPerdidos = qtdCigarros * minutosPerdidosCigarro * 365 * anosFumando
totalDiasPerdidos = totalMinutosPerdidos / (60 * 24)
print("total de minutos perdidos:", totalMinutosPerdidos, "| total de dias perdidos:", totalDiasPerdidos)