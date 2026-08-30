"""4 - Faça um programa que defina o array x = [1,2,3]. Faça uma cópia relacionada do array X para um array Z. Também copie o array x para o array y. Imprima os três na tela. Mude o segundo elemente do array y para 45 e o primeiro elemento do array X para 17. Imprima todos na tela novamente."""

x = [1, 2, 3]

z = x

y = x

print(x, z, y)

y[1] = 45

x[0] = 17

print(x, z, y)
