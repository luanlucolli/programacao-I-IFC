# Aguarda o usuário pressionar ENTER e limpa a tela do terminal.
def limpar_tela_desse_programa_super_legal():
    """Copie esta função no arquivo funcoes_super_legais_do_trabalho_final.py e importe ela no programa principal com o apelido limpar."""
    # função criada especificamente para limpar a tela após a execução de cada opção do menu
    import os

    # Pausa a execução até o usuário confirmar.
    input("Pressione ENTER para continuar…")
    # Limpa a tela no Windows ou em sistemas Unix.
    os.system("cls" if os.name == "nt" else "clear")
