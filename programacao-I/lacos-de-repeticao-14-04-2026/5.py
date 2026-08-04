'''5 - Faça um programa que calcule a soma e a média dos números de 223 até 445.'''

soma = 0
quantidade = 0

for i in range(223, 446):
    soma += i
    quantidade += 1

media = soma / quantidade

print("soma:", soma)
print("média:", media)
