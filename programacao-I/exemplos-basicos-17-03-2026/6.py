valor = float(input("valor: "))
desconto = float(input("desconto: "))
valorDesconto = valor * (desconto / 100)
valorFinal = valor - valorDesconto
print("valor desconto:", valorDesconto, "| valor final:", valorFinal)