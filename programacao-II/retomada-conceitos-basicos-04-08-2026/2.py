"""2 - Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Informe  A.M./P.M. Ao digitar 0 nos dois valores, o programa deve encerrar."""

while True:

    try:
        horas24 = int(input("informa as horas: "))
        minutos = int(input("insira os minutos: "))
    except:
        print("valores invalidos")
        print("")
    else:
        if horas24 == 0 and minutos == 0:
            break

        if horas24 >= 0 and horas24 <= 23 and minutos >= 0 and minutos <= 59:
            if horas24 >= 12:
                amOrPm = "P.M."
                if horas24 == 12:
                    horas12 = 12
                else:
                    horas12 = horas24 - 12
            else:
                amOrPm = "A.M."
                if horas24 == 0:
                    horas12 = 12
                else:
                    horas12 = horas24

            print(horas12, ":", minutos, amOrPm)
        else:
            print("horas ou minutos inválidos")
        print()
