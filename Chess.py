import chess
import random

class JogoXadrez:
    def __init__(self):
        self.tabuleiro = chess.Board()
        self.jogador_atual = None

    def fazer_movimento_aleatorio(self):
        movimentos_legais = list(self.tabuleiro.legal_moves)
        if movimentos_legais:
            movimento_aleatorio = random.choice(movimentos_legais)
            self.tabuleiro.push(movimento_aleatorio)
            return movimento_aleatorio

    def validar_movimento(self, movimento):
        # Verifica se o movimento é legal
        return chess.Move.from_uci(movimento) in self.tabuleiro.legal_moves

    def verificar_xeque_mate(self):
        # Verifica se a partida está em xeque-mate
        return self.tabuleiro.is_checkmate()

    def imprimir_tabuleiro(self):
        print(self.tabuleiro)

    def imprimir_jogada(self, movimento):
        print(f"Jogada do computador: {movimento.uci()}")

    def fazer_jogada_inicial(self):
        if self.jogador_atual == chess.WHITE:
            # Jogada inicial automática para as brancas
            self.fazer_movimento_aleatorio()
            self.imprimir_jogada(self.tabuleiro.move_stack[-1])
        else:
            # Jogada inicial automática para as pretas
            self.fazer_movimento_aleatorio()
            self.imprimir_jogada(self.tabuleiro.move_stack[-1])

    def escolher_lado(self):
        lado = input("Escolha as brancas (1) ou pretas (0): ").lower()
        if lado == '1':
            self.jogador_atual = chess.WHITE
            self.fazer_jogada_inicial()
        elif lado == '0':
            self.jogador_atual = chess.BLACK
            self.fazer_jogada_inicial()
        else:
            print("Escolha inválida. Por favor, escolha '1' para brancas ou '0' para pretas.")
            self.escolher_lado()

    def jogar(self):
        self.escolher_lado()

        while not self.tabuleiro.is_game_over():
            self.imprimir_tabuleiro()

            if self.tabuleiro.turn == self.jogador_atual:
                movimento = input("Digite seu movimento (por exemplo, 'e2 e4'): ")
                while not self.validar_movimento(movimento):
                    print("Movimento inválido. Tente novamente.")
                    movimento = input("Digite seu movimento (por exemplo, 'e2 e4'): ")

                self.tabuleiro.push_uci(movimento)
            else:
                movimento_computador = self.fazer_movimento_aleatorio()
                self.imprimir_jogada(movimento_computador)

            if self.verificar_xeque_mate():
                print("Xeque-mate! O jogo acabou.")
                break

        self.imprimir_tabuleiro()
        resultado = self.tabuleiro.result()
        print("Fim do jogo. Resultado: {}".format(resultado))

if __name__ == "__main__":
    jogo = JogoXadrez()
    jogo.jogar()
