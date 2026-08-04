dias = int(input("dias: "))
horas = int(input("horas: "))
minutos = int(input("minutos: "))
segundos = int(input("segundos: "))

totalSegundos = dias*24*60*60 + horas*60*60 + minutos*60 + segundos
print("total de segundos:", totalSegundos)