"""1 - Faça um programa que imprima na tela:
1
1   2
1   2   3
.....
1   2   3 ... n"""

try:
    numero = int(input("insira um número: "))
except:
    print("Valor inválido. Digite um número inteiro.")
else:
    if numero > 0:
        for i in range(1, numero + 1):
            for j in range(1, i + 1):
                print(f"{j}\t", end="")
            print()
    else:
        print("O número deve ser maior que 0.")
