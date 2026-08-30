"""2 - Faça um programa que defina os seguintes arrays: [42,41,40,39,38] , [55,54,56,53,51] e [0,0,0,0,0]. Depois faça a adição de cada elemento de índice correspondente do array (ex: 42+55, 41+54 e assim por diante). e armazene o resultado no array com zeros, substituindo cada um (por exemplo, o array de zeros vai ficando assim: [42+55, 41+5, 0,0,0]. Imprima na tela."""

numbers1 = [42, 41, 40, 39, 38]
numbers2 = [55, 54, 56, 53, 51]
numbers3 = [0, 0, 0, 0, 0]

for x in range(len(numbers3)):
    numbers3[x] = numbers1[x] + numbers2[x]
    
print(numbers3)
