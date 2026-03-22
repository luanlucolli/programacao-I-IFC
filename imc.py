altura = float(input("Altura: "))
peso = float(input("Peso: "))

if peso <= 0 or altura <= 0:
    print("Valores inválidos")
    exit()

imc = (peso / (altura * altura))

print("IMC:",round(imc,2))