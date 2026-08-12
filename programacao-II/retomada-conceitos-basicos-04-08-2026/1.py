"""1 - Solicite um número ao usuário e imprima na tela da seguinte forma:
1
2    2
3    3    3
n    n    n    ...n"""

numero = int(input("insira um número: "))

if numero > 0:
    for i in range(1, numero + 1):
        print(f"{i}\t" * i)

else:
    print("O número deve ser maior que 0.")
