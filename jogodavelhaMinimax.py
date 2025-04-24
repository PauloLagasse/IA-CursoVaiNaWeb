# Início

tabuleiro = [" " for _ in range(9)]  # Criar tabuleiro vazio com 9 posições

def exibir_tabuleiro():
    for i in range(0, 9, 3):
        print(tabuleiro[i], "|", tabuleiro[i+1], "|", tabuleiro[i+2])
    print()

def verificar_vencedor(tab, jogador):
    combinacoes_vencedoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]              # Diagonais
    ]
    return any(all(tab[pos] == jogador for pos in combinacao) for combinacao in combinacoes_vencedoras)

def verificar_empate(tab):
    return all(pos != " " for pos in tab)

def minimax(tab, profundidade, maximizando):
    if verificar_vencedor(tab, "X"):
        return -10 + profundidade
    if verificar_vencedor(tab, "O"):
        return 10 - profundidade
    if verificar_empate(tab):
        return 0

    if maximizando:
        melhor_valor = -float("inf")
        for i in range(9):
            if tab[i] == " ":
                tab[i] = "O"
                valor = minimax(tab, profundidade + 1, False)
                tab[i] = " "
                melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else:
        melhor_valor = float("inf")
        for i in range(9):
            if tab[i] == " ":
                tab[i] = "X"
                valor = minimax(tab, profundidade + 1, True)
                tab[i] = " "
                melhor_valor = min(melhor_valor, valor)
        return melhor_valor

def melhor_jogada(tab):
    melhor_valor = -float("inf")
    melhor_posicao = -1

    for i in range(9):
        if tab[i] == " ":
            tab[i] = "O"
            valor = minimax(tab, 0, False)
            tab[i] = " "
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_posicao = i

    return melhor_posicao

def jogar_jogo():
    print("Bem-vindo ao Jogo da Velha!")
    print("Você é o X e o computador é o O")
    print("As posições são numeradas de 0 a 8 da seguinte forma:")
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8\n")

    while True:
        exibir_tabuleiro()

        # Turno do jogador
        while True:
            try:
                jogada = int(input("Escolha sua jogada (0-8): "))
                if 0 <= jogada <= 8 and tabuleiro[jogada] == " ":
                    break
                else:
                    print("Jogada inválida. Tente novamente.")
            except:
                print("Entrada inválida. Use um número de 0 a 8.")

        tabuleiro[jogada] = "X"

        if verificar_vencedor(tabuleiro, "X"):
            exibir_tabuleiro()
            print("Você venceu!")
            break
        if verificar_empate(tabuleiro):
            exibir_tabuleiro()
            print("Empate!")
            break

        print("Computador está pensando...")
        melhor_posicao = melhor_jogada(tabuleiro)
        tabuleiro[melhor_posicao] = "O"

        if verificar_vencedor(tabuleiro, "O"):
            exibir_tabuleiro()
            print("O computador venceu!")
            break
        if verificar_empate(tabuleiro):
            exibir_tabuleiro()
            print("Empate!")
            break

# Execução inicial
jogar_jogo()

# Fim
