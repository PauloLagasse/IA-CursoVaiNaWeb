import sys

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("| " + " | ".join(linha) + " |")
    print()

def chegou_destino(linha, coluna):
    return linha == 0 and coluna == 7

def movimento_valido(tabuleiro, linha, coluna):
    return (
        0 <= linha < len(tabuleiro)
        and 0 <= coluna < len(tabuleiro[linha])
        and tabuleiro[linha][coluna] == " "
    )

# Função de simulação recursiva que retorna profundidade mínima até o destino
def buscar_melhor_movimento(tabuleiro, linha, coluna, visitado=None, profundidade=0):
    if chegou_destino(linha, coluna):
        return profundidade

    if visitado is None:
        visitado = set()

    visitado.add((linha, coluna))
    melhor_profundidade = float("inf")

    direcoes = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    for d_linha, d_coluna in direcoes:
        nova_linha = linha + d_linha
        nova_coluna = coluna + d_coluna

        if movimento_valido(tabuleiro, nova_linha, nova_coluna) and (nova_linha, nova_coluna) not in visitado:
            profundidade_resultado = buscar_melhor_movimento(
                tabuleiro, nova_linha, nova_coluna, visitado.copy(), profundidade + 1
            )
            if profundidade_resultado < melhor_profundidade:
                melhor_profundidade = profundidade_resultado

    return melhor_profundidade

# Essa função escolhe o melhor próximo passo (1 passo por vez)
def proximo_passo(tabuleiro, linha, coluna):
    melhor_profundidade = float("inf")
    melhor_linha = linha
    melhor_coluna = coluna

    direcoes = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    for d_linha, d_coluna in direcoes:
        nova_linha = linha + d_linha
        nova_coluna = coluna + d_coluna

        if movimento_valido(tabuleiro, nova_linha, nova_coluna):
            profundidade = buscar_melhor_movimento(tabuleiro, nova_linha, nova_coluna)
            if profundidade < melhor_profundidade:
                melhor_profundidade = profundidade
                melhor_linha = nova_linha
                melhor_coluna = nova_coluna

    return melhor_linha, melhor_coluna

def main():
    tabuleiro = [
        ['x', ' ', ' ', ' ', ' ', ' ', 'x', ' '],
        [' ', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', 'x', ' ', ' ', ' ', ' ', 'x', ' '],
        ['x', ' ', ' ', 'x', ' ', 'x', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', ' ', ' ', ' '],
        [' ', 'x', ' ', 'x', ' ', 'x', ' ', ' '],
        [' ', 'x', ' ', 'x', ' ', 'x', ' ', ' '],
        [' ', 'x', ' ', ' ', ' ', 'x', ' ', ' '],
    ]

    linha, coluna = 7, 0  # posição inicial
    tabuleiro[linha][coluna] = "*"
    mostrar_tabuleiro(tabuleiro)

    while not chegou_destino(linha, coluna):
        sys.stdin.read(1)  # Espera ENTER
        nova_linha, nova_coluna = proximo_passo(tabuleiro, linha, coluna)

        if (nova_linha, nova_coluna) == (linha, coluna):
            print("Caminho bloqueado. Não é possível continuar.")
            break

        linha, coluna = nova_linha, nova_coluna
        tabuleiro[linha][coluna] = "*"
        print(f"proxima linha = {linha}, proxima coluna = {coluna}, profundidade = ")
        mostrar_tabuleiro(tabuleiro)

    print("Destino alcançado!")

main()
