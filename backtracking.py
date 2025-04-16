import sys
def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("| " + " | ".join(linha) + " |")

def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade):
    #Armazena a melhor profundidade, começando com o maior valor possivel
    melhor_profundidade = float("inf")

    #Melhor linha e coluna a ser retornada
    melhor_linha = linha_atual
    melhor_coluna = coluna_atual

    #Movimentação para a direita
    proxima_linha = linha_atual
    proxima_coluna = coluna_atual + 1

    #verificar se o movimento é valido
    if movimento_valido(tabuleiro, proxima_linha, proxima_coluna):
        if chegou_destino(proxima_linha, proxima_coluna): #Verificar se chegou ao destino
            return [proxima_linha, proxima_coluna, profundidade]
        
        tabuleiro[proxima_linha][proxima_coluna] = "*"
        resultado_movimento = proximo_movimento(tabuleiro, proxima_linha, proxima_coluna, profundidade + 1)
        tabuleiro[proxima_linha][proxima_coluna] = " "

        if resultado_movimento[2] < melhor_profundidade:
            melhor_linha = proxima_linha
            melhor_coluna = proxima_coluna
            melhor_profundidade = resultado_movimento[2]

    #Movimento para a esquerda
    proxima_linha = linha_atual
    proxima_coluna = coluna_atual - 1

    if movimento_valido(tabuleiro, proxima_linha, proxima_coluna):
        if chegou_destino(proxima_linha, proxima_coluna): #Verificar se chegou ao destino
            return [proxima_linha, proxima_coluna, profundidade]
        
        tabuleiro[proxima_linha][proxima_coluna] = "*"
        resultado_movimento = proximo_movimento(tabuleiro, proxima_linha, proxima_coluna, profundidade + 1)
        tabuleiro[proxima_linha][proxima_coluna] = " "

        if resultado_movimento[2] < melhor_profundidade:
            melhor_linha = proxima_linha
            melhor_coluna = proxima_coluna
            melhor_profundidade = resultado_movimento[2]

    #Movimento para cima (NIVEL MESMO DA DIREITA)
    proxima_linha = linha_atual - 1
    proxima_coluna = coluna_atual 

    if movimento_valido(tabuleiro, proxima_linha, proxima_coluna):
        if chegou_destino(proxima_linha, proxima_coluna): #Verificar se chegou ao destino
            return [proxima_linha, proxima_coluna, profundidade]
        
        tabuleiro[proxima_linha][proxima_coluna] = "*"
        resultado_movimento = proximo_movimento(tabuleiro, proxima_linha, proxima_coluna, profundidade + 1)
        tabuleiro[proxima_linha][proxima_coluna] = " "

        if resultado_movimento[2] < melhor_profundidade:
            melhor_linha = proxima_linha
            melhor_coluna = proxima_coluna
            melhor_profundidade = resultado_movimento[2]

    #Movimento para baixo (NIVEL MESMO DA DIREITA)
    proxima_linha = linha_atual + 1
    proxima_coluna = coluna_atual 

    if movimento_valido(tabuleiro, proxima_linha, proxima_coluna):
        if chegou_destino(proxima_linha, proxima_coluna): #Verificar se chegou ao destino
            return [proxima_linha, proxima_coluna, profundidade]
        
        tabuleiro[proxima_linha][proxima_coluna] = "*"
        resultado_movimento = proximo_movimento(tabuleiro, proxima_linha, proxima_coluna, profundidade + 1)
        tabuleiro[proxima_linha][proxima_coluna] = " "

        if resultado_movimento[2] < melhor_profundidade:
            melhor_linha, melhor_coluna, melhor_profundidade = resultado_movimento
    
    return [melhor_linha, melhor_coluna, melhor_profundidade]

#Verificando se o moviento é valido dentro dos limites do tabuleiro (linhas e colunas). Retorna False caso o movimento ultrapasse o tamanho do tabuleiro
def movimento_valido(tabuleiro, linha, coluna) -> bool:
    return 0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[linha]) and tabuleiro[linha][coluna] == " "

def chegou_destino(linha, coluna):
    return linha == 0 and coluna == 7

def main():
    tabuleiro = [
        ['x', ' ', ' ', ' ', ' ', ' ', 'x', ' '],
        [' ', ' ', 'x', ' ', 'x', ' ', ' ', ' '],
        [' ', 'x', ' ', ' ', ' ', ' ', 'x', ' '],
        ['x', ' ', ' ', 'x', ' ', 'x', ' ', ' '],
        [' ', ' ', ' ', 'x', ' ', ' ', ' ', ' '],
        [' ', 'x', ' ', 'x', ' ', 'x', ' ', ' '],
        [' ', 'x', ' ', 'x', ' ', 'x', ' ', ' '],
        [' ', 'x', ' ', ' ', ' ', 'x', ' ', ' '],
    ]

    proxima_linha = 7 #linha de onde vc vai comecar 
    proxima_coluna = 0 #coluna de onde vc vai comecar 

    tabuleiro[proxima_linha][proxima_coluna] = "*"

    mostrar_tabuleiro(tabuleiro)
    import sys
    while sys.stdin.read(1) and not chegou_destino(proxima_linha, proxima_coluna):
        melhor_movimento = proximo_movimento(tabuleiro, proxima_linha, proxima_coluna, 0)

        linha, coluna, profundidade = melhor_movimento

        if profundidade == float("inf"):
            print("Não é possivel encontrar um caminho")
            break

        print(f"proxima linha = {linha}, proxima coluna = {coluna}, profundidade = {profundidade}")

        #Mantem a melhor linha e a melhor coluna marcada
        tabuleiro[linha][coluna] = "*"
        proxima_linha = linha
        proxima_coluna = coluna
        mostrar_tabuleiro(tabuleiro)

main()