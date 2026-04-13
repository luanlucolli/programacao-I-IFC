#2 - Faça um programa onde o usuário deverá digitar um número. 
# Depois informe se o número digitado é par ou impar. 
# Adicionalmente, verifique se o número é divisível por 3.

numero = int(input("numero: "))

if numero %2 == 0:
    print(numero, "é par")
else:
    print(numero, "é ímpar")