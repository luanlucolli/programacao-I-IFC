valorDiaAluguel = 60
valorKmRodado = 0.15

kmPercorrido = float(input("km percorrido: "))
diasPercorridos = int(input("dias percorridos: "))

valorTotal = (valorDiaAluguel * diasPercorridos) + (valorKmRodado * kmPercorrido)
print("valor total do aluguel:", valorTotal)