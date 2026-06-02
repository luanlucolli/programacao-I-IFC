

def soma():
    print("")
    try:
        n1 = int(input("n1: "))
        n2 = int(input("n2: "))
    except:
        print("valores inválidos\n")
    else:
        print("soma:",n1+n2)
        
def subtracao():
    print("")
    try:
        n1 = int(input("n1: "))
        n2 = int(input("n2: "))
    except:
        print("valores inválidos\n")
    else:
        print("subtração:",n1-n2)
        
def multiplicacao():
    print("")
    try:
        n1 = int(input("n1: "))
        n2 = int(input("n2: "))
    except:
        print("valores inválidos\n")
    else:
        print("multiplicação:",n1*n2)
        
def divisao():
    print("")
    try:
        n1 = int(input("n1: "))
        n2 = int(input("n2: "))
    except:
        print("valores inválidos\n")
    else:
        print("divisão:",n1/n2)
        
def resto():
    print("")
    try:
        n1 = int(input("n1: "))
        n2 = int(input("n2: "))
    except:
        print("valores inválidos\n")
    else:
        print("resto:",n1%n2)
        
def exponenciacao():
    print("")
    try:
        n1 = int(input("n1: "))
        n2 = int(input("n2: "))
    except:
        print("valores inválidos\n")
    else:
        print("exponenciação:",n1**n2)
        
def raizQuadrada():
    print("")
    try:
        n1 = int(input("n1: "))
    except:
        print("valores inválidos\n")
    else:
        print("raiz quadrada::",n1 ** 0.5)
        
def somatorio():
    print("")
    try:
        n1 = int(input("n1: "))
    except:
        print("valores inválidos\n")
    else:
        soma = 0
        for i in range(n1+1):
            soma = soma + i
    
        print(soma)
