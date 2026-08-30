"""1 - Faça um programa que defina o seguinte array: [4,5,6,8,7]. Depois faça a subtração de cada elemento do array por 1, resultando o array [3,4,5,7,6]. Imprima ambos na tela."""

numbers = [4,5,6,8,7]

print(numbers)

for x in range(len(numbers)):
    numbers[x]-= 1
    
print(numbers)
