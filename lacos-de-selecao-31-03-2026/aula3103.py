def comparar_dois_numeros():
    numero1 = int(input("numero 1: "))
    numero2 = int(input("numero 2: "))

    if numero1 == numero2:
        print("os números são iguais")
    elif numero1 > numero2:
        print(numero1, "é maior que", numero2)
    else:
        print(numero2, "é maior que", numero1)


def verificar_par_impar_divisivel_por_tres():
    numero = int(input("numero: "))

    if numero % 2 == 0:
        print(numero, "é par")
    else:
        print(numero, "é ímpar")

    if numero % 3 == 0:
        print("o número é divisível por 3")
    else:
        print("o número não é divisível por 3")


def ordenar_tres_numeros():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    n3 = int(input("numero 3: "))

    if n1 > n2:
        if n1 > n3:
            maior = n1
            if n2 > n3:
                meio = n2
                menor = n3
            else:
                meio = n3
                menor = n2
        else:
            maior = n3
            meio = n1
            menor = n2
    elif n2 > n3:
        maior = n2
        if n3 > n1:
            meio = n3
            menor = n1
        else:
            meio = n1
            menor = n3
    else:
        maior = n3
        meio = n2
        menor = n1

    print(menor)
    print(meio)
    print(maior)


def mostrar_mes_por_numero():
    numero = int(input("informe um número de 1 a 12: "))

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


def classificar_faixa_etaria():
    idade = int(input("idade: "))

    if idade >= 0:
        if idade <= 5:
            print("Bebê ou infante")
        elif idade <= 11:
            print("Criança")
        elif idade <= 17:
            print("Adolescente")
        elif idade <= 24:
            print("Jovem")
        elif idade <= 49:
            print("Adulto")
        elif idade <= 65:
            print("Senior")
        else:
            print("Idoso")
    else:
        print("Idade inválida")


def calcular_imc():
    peso = float(input("peso: "))
    altura = float(input("altura: "))

    imc = peso / (altura * altura)
    print("IMC:", imc)

    if imc >= 0:
        if imc < 18:
            print("Possível desnutrição")
        elif imc <= 24:
            print("Peso aparentemente normal")
        elif imc <= 29:
            print("Possível sobrepeso")
        elif imc <= 34:
            print("Possível obesidade")
        else:
            print("Obesidade")
    else:
        print("IMC inválido")
