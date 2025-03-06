from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax
import random

class ClumsyConnectFour(TwoPlayerGame):
    def __init__(self, players=None):
        self.players = players
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 1  # Gracz 1 zaczyna

    def possible_moves(self):
        return [str(c) for c in range(7) if self.board[0][c] == ' ']

    def make_move(self, column):
        column = int(column)
        actual_column = self.probabilistic_column(column)

        for row in reversed(range(6)):
            if self.board[row][actual_column] == ' ':
                self.board[row][actual_column] = self.current_player_symbol()
                break

    def probabilistic_column(self, column):
        roll = random.random()
        if roll < 0.1 and column > 0:
            return column - 1
        elif roll < 0.2 and column < 6:
            return column + 1
        return column

    def current_player_symbol(self):
        return 'X' if self.current_player == 1 else 'O'

    def unmake_move(self, column):
        column = int(column)
        for row in range(6):
            if self.board[row][column] != ' ':
                self.board[row][column] = ' '
                break

    def show(self):
        for row in self.board:
            print("|" + "|".join(row) + "|")
        print(" " + " ".join(map(str, range(7))))

    def lose(self):
        return self.four_in_a_row(self.current_player_symbol())

    def is_over(self):
        return self.possible_moves() == [] or self.lose()

    def scoring(self):
        if self.lose():
            return -100
        return 0

    def four_in_a_row(self, symbol):
        for row in range(6):
            for col in range(4):
                if all(self.board[row][col+i] == symbol for i in range(4)):
                    return True

        for row in range(3):
            for col in range(7):
                if all(self.board[row+i][col] == symbol for i in range(4)):
                    return True

        for row in range(3):
            for col in range(4):
                if all(self.board[row+i][col+i] == symbol for i in range(4)):
                    return True
                if all(self.board[row+3-i][col+i] == symbol for i in range(4)):
                    return True

        return False
