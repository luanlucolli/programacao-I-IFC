'''6 - Faça os mesmos exercícios utilizando o While.'''

print("Exercício 1")
numero = int(input("insira um número: "))
i = 0

while i <= numero:
    print(i)
    i += 1

print("\nExercício 2")
numero = int(input("insira um número: "))
i = 0

while i <= numero:
    if i % 2 == 0:
        print(i)
    i += 1

print("\nExercício 3")
i = 1

while i <= 1000:
    if i % 2 != 0:
        print(i)

    if i + 2 <= 1000 and (i + 2) % 2 != 0:
        print(i + 2)

    i += 3

print("\nExercício 4")
numero1 = int(input("primeiro número: "))
numero2 = int(input("segundo número: "))
resultado = 0
contador = 0

while contador < numero1:
    resultado += numero2
    contador += 1

print("resultado:", resultado)

print("\nExercício 5")
soma = 0
quantidade = 0
numero = 223

while numero <= 445:
    soma += numero
    quantidade += 1
    numero += 1

media = soma / quantidade

print("soma:", soma)
print("média:", media)
