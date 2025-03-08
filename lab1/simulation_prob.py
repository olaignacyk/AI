import numpy as np
from easyAI import AI_Player, Negamax
from ConnectFourFinal import ClumsyConnectFour


def run_games_with_probabilistic_clumsy(depth1, depth2, num_games=50):
    """
    Funkcja symulująca rozgrywki ClumsyConnectFour dla dwóch graczy AI
    z różnymi głębokościami Negamax. Gracze zmieniają się w rozpoczynaniu.
    """
    results = {1: 0, 2: 0, 'draw': 0}

    for game_number in range(num_games):
        # Zmiana gracza rozpoczynającego co grę
        if game_number % 2 == 0:
            players = [AI_Player(Negamax(depth1)), AI_Player(Negamax(depth2))]
        else:
            players = [AI_Player(Negamax(depth2)), AI_Player(Negamax(depth1))]

        game = ClumsyConnectFour(players)
        game.play()

        if game.lose():
            winner = game.opponent_index  # Przegrywający to current_player, więc wygrywa opponent_index
            results[winner] += 1
        else:
            results['draw'] += 1

    return results


if __name__ == "__main__":
    num_games = 2  # Liczba gier do rozegrania
    depth1 = 3  # Głębokość wyszukiwania dla gracza 1
    depth2 = 5  # Głębokość wyszukiwania dla gracza 2

    print(f"⚙️  Symulacja {num_games} gier w ClumsyConnectFour z probabilistycznym przesuwaniem.")
    print(f"Gracz 1: Negamax({depth1})")
    print(f"Gracz 2: Negamax({depth2})\n")

    results = run_games_with_probabilistic_clumsy(depth1, depth2, num_games)

    print(f"📊 Wyniki:")
    print(f"Gracz 1 wygrał: {results[1]} razy")
    print(f"Gracz 2 wygrał: {results[2]} razy")
    print(f"Remisy: {results['draw']}")

    print("\n📈 Podsumowanie:")
    print(f"Zwycięstwa Gracza 1: {results[1] / num_games * 100:.1f}%")
    print(f"Zwycięstwa Gracza 2: {results[2] / num_games * 100:.1f}%")
    print(f"Remisy: {results['draw'] / num_games * 100:.1f}%")
