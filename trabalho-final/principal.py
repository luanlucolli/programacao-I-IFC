import funcoes_gerais as fng
import funcoes_especificas as fne

def menu():
    
    op = ""
    
    while op != 0 and op != "S" and op != "s":
        
        print("Opções:")
        print("S ou 0 - Sair")
        print("M ou 1 - Dias")
        print("E ou 2 - Expressões Matemáticas")
        print("F ou 3 - F0, F1, F2 ou F3")
        print("A ou 4 - Somatório e Média")
        print("P ou 5 - Par ou Ìmpar")
        print("X ou 6 - Operações Matemáticas")

        op = input("Escolha uma das opções: ")
        
        match op:
            case "S" | "s" | 0:
                fng.fim_prog()
            case "M" | "m" | 1:
                print("dias")
            case "E" | "e" | 2:
                print("expressões matematicas")            
            case "F" | "f" | 3:
                print("f0,f1,f2,f3")
            case "A" | "a" | 4:
                print("somatorio ou media")
            case "P" | "p" | 5:
                print("par ou impar")   
            case "X" | "x" | 6:
                print("operacoes matematicas")   
                
# Função principal                 
def main():
    fng.inicio_prog()
    menu()
    
print(fng.somatorio(10))
print(fng.media_somatorio(10))