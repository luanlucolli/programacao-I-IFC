''' 5 - Escreva um programa que deverá perguntar a idade do usuário. Verifique se o usuário digitou de fato um número. 
Caso não, emita um aviso na tela e encerre o programa.  Depois imprima na tela segundo as instruções abaixo:
- Caso a idade esteja entre 0 e 5 anos, imprimir: "Bebê ou infante",
- Caso a idade esteja entre 6 e 11 anos, imprimir: "Criança",
- Caso a idade esteja entre 12 e 17 anos, imprimir: "Adolescente",
- Caso a idade esteja entre 18 e 24 anos, imprimir: "Jovem",
- Caso a idade esteja entre 25 e 49 anos, imprimir: "Adulto",
- Caso a idade esteja entre 50 e 65 anos, imprimir: "Senior",
- Caso a idade esteja acima de 65 anos, imprimir: "Idoso". '''

idade = int(input("idade: "))

if idade >= 0:
    if idade <= 5:
        print("Bebê ou infante")
    elif idade <= 11:
        print("Criança")
    elif idade <= 17:
        print("Adolescente")
    elif idade <= 24:
        print("Jovem")
    elif idade <= 49:
        print("Adulto")
    elif idade <= 65:
        print("Senior")
    else:
        print("Idoso")    
else:
    print("Idade inválida")