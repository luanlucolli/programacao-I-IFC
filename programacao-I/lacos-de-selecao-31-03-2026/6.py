''' 5 - Escreva um programa que deverá calcular o IMC do usuário. Ele deverá informar o peso e altura. 
A fórmula do IMC é peso / altura ao quadrado. 
Conforme o resultado, deverá ser impresso na tela o valor do IMC e também a seguinte frase:
- Caso o IMC esteja abaixo de 18, imprimir: "Possível Desnutrição",
- Caso o IMC esteja entre 18 e 24, imprimir: "Peso aparentemente normal",
- Caso o IMC esteja entre 25 e 29, imprimir: "Possível Sobrepeso",
- Caso o IMC esteja entre 30 e 34, imprimir: "Possível Obesidade",
- Caso o IMC esteja acima de 35, imprimir: "Obesidade cronica". '''

peso = float(input("peso: "))
altura = float(input("altura: "))

imc = peso / (altura * altura)
print("IMC:",imc)

if imc >= 0:
    if imc < 18:
        print("Possível desnutrição")
    elif imc <= 24:
        print("Peso aparentemente normal")
    elif imc <= 29:
        print("Possível sobrepeso")
    elif imc <= 34:
        print("Possível obesidade")
    else: 
        print("Obesidade")
else:
    print("IMC inválido")
    