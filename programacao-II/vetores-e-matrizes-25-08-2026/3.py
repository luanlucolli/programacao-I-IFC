"""3 - Faça um programa que gere o segiunte array: [0,0,0,0]. Substitua os valores zerados por números aleatórios. Imprima o array na tela. Depois apresente o somátório e a média do array de números aleatórios."""

from random import randint

numbers = [0, 0, 0, 0]
soma = 0
media = 0
numbersLen = len(numbers)

for x in range(numbersLen):
    numbers[x] = randint(0, 999)
    soma += numbers[x]
    if x == numbersLen - 1:
        media = soma / numbersLen

print(numbers)
print(soma)
print(media)
