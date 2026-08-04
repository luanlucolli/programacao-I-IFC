'''2 - Faça um algoritmo onde o usuário deverá digitar um número. 
O programa deverá listar todos os números pares até o número digitado pelo usuário.'''

numero = int(input("insira um número: "))

for i in range(numero+1):
    if i % 2 == 0:
        print(i)