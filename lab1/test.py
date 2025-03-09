import numpy as np
import time
from easyAI import TwoPlayerGame, AI_Player, Negamax, TranspositionTable
from ConnectFourFinal import ClumsyConnectFour
from program import ConnectFour
import pandas as pd



def run_games_with_stats(depth,  use_alpha_beta=True, probabilistic=True, num_games=50):
    results = {1: 0, 2: 0, 'draw': 0}
    start_time = time.time()
    for game_number in range(num_games):
            if use_alpha_beta:
                tt = TranspositionTable()
                player1 = AI_Player(Negamax(depth, tt=tt))
                player2 = AI_Player(Negamax(depth, tt=tt))
            else:
                player1 = AI_Player(Negamax(depth))
                player2 = AI_Player(Negamax(depth))
            
            players = [player1, player2] if game_number % 2 == 0 else [player2, player1]
            game = ConnectFour(players) if not probabilistic else ClumsyConnectFour(players)
            game.play()
            
            if game.lose():
                winner = game.opponent_index
                results[winner] += 1
            else:
                results['draw'] += 1
        
    end_time = time.time()
    execution_time = end_time - start_time
        
    return {
        "Depth": f"{depth}",
        "Probabilistic": probabilistic,
        "Alpha-Beta Pruning": use_alpha_beta,
        "Player 1 Wins": results[1],
        "Player 2 Wins": results[2],
        "Draws": results['draw'],
        "Execution Time (s)": execution_time
        }

if __name__ == "__main__":
    num_games = 5

    stats = []
    
    stats.append(run_games_with_stats(3, True, True, num_games))
    stats.append(run_games_with_stats(5, True, True, num_games))
    stats.append(run_games_with_stats(3, False, True, num_games))
    stats.append(run_games_with_stats(5, False, True, num_games))
    stats.append(run_games_with_stats(3, True, False, num_games))
    stats.append(run_games_with_stats(5, True, False, num_games))
    stats.append(run_games_with_stats(3, False, False, num_games))
    stats.append(run_games_with_stats(5, False, False, num_games))    
    
    df = pd.DataFrame(stats)
    print(df)
    df.to_csv("game_statistics.csv", index=False)
