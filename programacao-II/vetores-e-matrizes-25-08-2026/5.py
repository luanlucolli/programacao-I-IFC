"""5 - Faça um programa que defina o array V = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]. Substitua todos os zeros por números aleatórios. Depois, imprima na tela somente os números pares do array."""

import random

V = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in range(len(V)):
    V[x] = random.randint(0, 999)
    if V[x] % 2 == 0:
        print(V[x])
