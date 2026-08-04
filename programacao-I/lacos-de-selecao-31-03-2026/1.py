'''1 - Faça um programa onde o usuário deverá digitar dois números. 
Verifique qual dos dois números é maior e imprima na tela informando qual é o maior.'''

numero1 = int(input("numero 1: "))
numero2 = int(input("numero 2: "))

if numero1 == numero2:
    print("os números são iguais")
elif numero1 > numero2:
    print(numero1,"é maior que",numero2)
else:
    print(numero2,"é maior que",numero1)