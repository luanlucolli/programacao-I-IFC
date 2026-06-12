def limpar_tela_desse_programa_super_legal():
    # função criada especificamente para limpar a tela após a execução de cada opção do menu
    import os

    input("Pressione ENTER para continuar…")
    os.system("cls" if os.name == "nt" else "clear")
