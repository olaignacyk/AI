import time
import numpy as np
from easyAI import TwoPlayerGame, AI_Player, Negamax, TranspositionTable
from ConnectFourFinal import ClumsyConnectFour

class ExpectiMinimaxAI(AI_Player):
    """ Expecti-Minimax AI z odcięciem alfa-beta """

    def __init__(self, depth):
        super().__init__(None)  # `easyAI` wymaga wywołania konstruktora `AI_Player`
        self.depth = depth

    def expecti_minimax(self, game, depth, alpha, beta, maximizing_player):
        if depth == 0 or game.is_over():
            return game.scoring(), None

        moves = game.possible_moves()
        best_move = moves[0]

        if maximizing_player:
            max_eval = -np.inf
            for move in moves:
                new_game = game.copy()
                new_game.make_move(move)
                eval, _ = self.expecti_minimax(new_game, depth - 1, alpha, beta, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = np.inf
            for move in moves:
                new_game = game.copy()
                new_game.make_move(move)
                eval, _ = self.expecti_minimax(new_game, depth - 1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def ask_move(self, game):
        """ Wymagana przez `easyAI` metoda zwracająca najlepszy ruch """
        _, best_move = self.expecti_minimax(game, self.depth, -np.inf, np.inf, True)
        return best_move


def test_algorithms(depth=3, num_games=5):
    """ Test porównujący Expecti-Minimax i Negamax """
    results = {"Expecti-Minimax": {"Wins": 0, "Losses": 0, "Draws": 0, "Time": 0},
               "Negamax": {"Wins": 0, "Losses": 0, "Draws": 0, "Time": 0}}

    for algo_name, ai in [("Expecti-Minimax", ExpectiMinimaxAI(depth)), 
                          ("Negamax", AI_Player(Negamax(depth)))]:
        start_time = time.time()
        for _ in range(num_games):
            game = ClumsyConnectFour([ai, AI_Player(Negamax(depth))])
            game.play()
            if game.lose():
                results[algo_name]["Wins"] += 1
            elif game.is_over():
                results[algo_name]["Draws"] += 1
            else:
                results[algo_name]["Losses"] += 1

        results[algo_name]["Time"] = time.time() - start_time

    return results


# Uruchomienie testu
comparison_results = test_algorithms(depth=5, num_games=5)

# Wyświetlenie wyników
import pandas as pd
df_results = pd.DataFrame(comparison_results).T
print(df_results)
