from ConnectFourFinal import ClumsyConnectFour
from easyAI import AI_Player, Negamax
import time

def simulate_games(n, depth1, depth2):
    results = {"Player 1": 0, "Player 2": 0, "Draw": 0}
    times = []

    for _ in range(n):
        game = ClumsyConnectFour(
            [AI_Player(Negamax(depth1)), AI_Player(Negamax(depth2))]
        )
        start_time = time.time()
        game.play()
        duration = time.time() - start_time
        times.append(duration)

        if game.lose():
            winner = f"Player {game.opponent_index}"
            results[winner] += 1
        else:
            results["Draw"] += 1

    avg_time = sum(times) / len(times)
    return results, avg_time


if __name__ == "__main__":
    for depth in [3, 5]:
        print(f"\nSimulating 3 games with depth {depth} vs {depth}")
        results, avg_time = simulate_games(3, depth, depth)
        print("Results:", results)
        print(f"Average time per game: {avg_time:.2f} seconds")
