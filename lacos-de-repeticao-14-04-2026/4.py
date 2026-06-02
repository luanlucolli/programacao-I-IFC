'''4 - Faça um programa que solicite dois números ao usuário.
Utiliza uma multiplicação por somatória.
Ex: o usuário digita 3 e 4. logo, deverá somar 4+4+4.'''

numero1 = int(input("primeiro número: "))
numero2 = int(input("segundo número: "))

resultado = 0

for i in range(numero1):
    resultado += numero2

print("resultado:", resultado)
