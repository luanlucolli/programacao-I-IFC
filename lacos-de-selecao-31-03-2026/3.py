'''3 - Escreva um programa que deverá perguntar três números ao usuário. 
Imprima estes números em ordem crescente (do menor para o maior)'''

n1 = int(input("numero 1: "))
n2 = int(input("numero 2: "))
n3 = int(input("numero 3: "))

maior = None
meio = None
menor = None

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