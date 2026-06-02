'''3 - Faça um algoritmo que liste todos os números ímpares até 1000.
Utilize um laço de repetição que faça incrementos de 3 em 3.'''

for i in range(1, 1001, 3):
    if i % 2 != 0:
        print(i)

    if i + 2 <= 1000 and (i + 2) % 2 != 0:
        print(i + 2)
