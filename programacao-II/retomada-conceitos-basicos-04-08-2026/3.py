"""3 - Faça um programa onde o usuário deverá registrar 5 valores de depósito
positivos bancários. Ao final, imprima na tela o maior valor, o menor, a soma
e a média.
"""

quantidade = 0
soma = 0
maior = 0
menor = 0

while quantidade < 5:
    deposito = float(input("Informe um depósito: "))

    if deposito > 0:
        quantidade += 1
        soma += deposito

        if quantidade == 1:
            maior = deposito
            menor = deposito
        else:
            if deposito > maior:
                maior = deposito

            if deposito < menor:
                menor = deposito
    else:
        print("O valor do depósito deve ser positivo.")

media = soma / quantidade

print("Maior valor: R$", maior)
print("Menor valor: R$", menor)
print("Soma: R$", soma)
print("Média: R$", media)
