numero = input("informe um número de 1 a 12")

if numero >= 1 and numero <= 12:
    if numero == 1:
        print("janeiro")
    elif numero == 2:
        print("fevereiro")
    elif numero == 3:
        print("março")
    elif numero == 4:
        print("abril")
    elif numero == 5:
        print("maio")
    elif numero == 6:
        print("junho")
    elif numero == 7:
        print("julho")
    elif numero == 8:
        print("agosto")
    elif numero == 9:
        print("setembro")
    elif numero == 10:
        print("outubro")
    elif numero == 11:
        print("novembro")
    else:
        print("dezembro")
else:
    print("número inválido")