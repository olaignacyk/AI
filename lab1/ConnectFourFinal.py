try:
    import numpy as np
except ImportError:
    print("Sorry, this example requires Numpy installed!")
    raise

from easyAI import TwoPlayerGame
from termcolor import colored

class ClumsyConnectFour(TwoPlayerGame):
    """
    Clumsy Connect Four - żeton może spaść do sąsiedniej kolumny z 10% szansą.
    """

    def __init__(self, players, board=None):
        self.players = players
        self.board = (
            board
            if (board is not None)
            else (np.array([[0 for i in range(7)] for j in range(6)]))
        )
        self.current_player = 1  # player 1 starts.
        self.winning_positions = None  # Zapisz zwycięskie pola (jeśli są)

    def possible_moves(self):
        """Zwraca listę kolumn, do których można wrzucić żeton."""
        return [i for i in range(7) if (self.board[:, i].min() == 0)]

    def make_move(self, column):
        """Wrzucenie żetonu z mechanizmem 'rozjeżdżania'."""
        column = self.apply_probabilistic_shift(column)
        line = np.argmin(self.board[:, column] != 0)
        self.board[line, column] = self.current_player

    def apply_probabilistic_shift(self, column):
        """Z 10% szansą przesuwa żeton w lewo lub w prawo, jeśli to możliwe."""
        roll = np.random.random()
        if roll < 0.1 and column > 0:
            return column - 1
        elif roll < 0.2 and column < 6:
            return column + 1
        return column

    def show(self):
        """
        Wyświetla planszę, podświetlając zwycięskie żetony (jeśli istnieją).
        """
        self.winning_positions = find_four(self.board, self.opponent_index)

        print("\n" + "\n".join(
            ["0 1 2 3 4 5 6", 13 * "-"] +
            [
                " ".join([
                    self.colored_token(5 - j, i)
                    for i in range(7)
                ])
                for j in range(6)
            ]
        ))

    def colored_token(self, row, col):
        """
        Zwraca żeton z kolorowaniem, jeśli jest częścią zwycięskiej czwórki.
        """
        token = self.board[row][col]
        if token == 0:
            return "."
        elif (row, col) in (self.winning_positions or []):
            return colored("O" if token == 1 else "X", "red")
        else:
            return "O" if token == 1 else "X"

    def lose(self):
        """Czy obecny gracz przegrał (czy przeciwnik wygrał)."""
        self.winning_positions = find_four(self.board, self.opponent_index)
        return self.winning_positions is not None

    def is_over(self):
        """Czy gra się zakończyła."""
        return (self.board.min() > 0) or self.lose()

    def scoring(self):
        """Ocena stanu gry dla algorytmu Negamax."""
        return -100 if self.lose() else 0


def find_four(board, player):
    """
    Znajduje linię 4 żetonów jednego gracza.
    Zwraca listę współrzędnych [(row, col), ...] albo None jeśli brak wygranej.
    """
    for pos, direction in POS_DIR:
        streak = 0
        winning_positions = []

        while 0 <= pos[0] <= 5 and 0 <= pos[1] <= 6:
            if board[pos[0], pos[1]] == player:
                streak += 1
                winning_positions.append((pos[0], pos[1]))
                if streak == 4:
                    return winning_positions  
            else:
                streak = 0
                winning_positions = []
            pos = pos + direction

    return None


POS_DIR = np.array(
    [[[i, 0], [0, 1]] for i in range(6)]  # poziomo
    + [[[0, i], [1, 0]] for i in range(7)]  # pionowo
    + [[[i, 0], [1, 1]] for i in range(1, 3)]  # skos ↘️
    + [[[0, i], [1, 1]] for i in range(4)]
    + [[[i, 6], [1, -1]] for i in range(1, 3)]  # skos ↙️
    + [[[0, i], [1, -1]] for i in range(3, 7)]
)

if __name__ == "__main__":
    from easyAI import AI_Player, Negamax

    ai_algo_negamax = Negamax(3)

    game = ClumsyConnectFour([AI_Player(ai_algo_negamax), AI_Player(ai_algo_negamax)])
    game.play()

    if game.lose():
        print(f"Player {game.opponent_index} wins.")
    else:
        print("Looks like we have a draw.")
