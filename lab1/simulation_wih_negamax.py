import numpy as np
from easyAI import AI_Player, Negamax
from ConnectFourFinal import ClumsyConnectFour
from program import ConnectFour

def run_games_with_probabilistic_clumsy(depth1, depth2, probabilistic=True, num_games=50):
    """
    Funkcja symulująca rozgrywki ClumsyConnectFour lub ConnectFour dla dwóch graczy AI
    z różnymi głębokościami Negamax. Gracze zmieniają się w rozpoczynaniu.
    """
    results = {1: 0, 2: 0, 'draw': 0}

    for game_number in range(num_games):
        # Zmiana gracza rozpoczynającego co grę
        if game_number % 2 == 0:
            players = [AI_Player(Negamax(depth1)), AI_Player(Negamax(depth2))]
        else:
            players = [AI_Player(Negamax(depth2)), AI_Player(Negamax(depth1))]

        game = ClumsyConnectFour(players) if probabilistic else ConnectFour(players)
        game.play()

        if game.lose():
            winner = game.opponent_index  # Przegrywający to current_player, więc wygrywa opponent_index
            results[winner] += 1
        else:
            results['draw'] += 1

    return results

if __name__ == "__main__":
    num_games = 5  # Liczba gier do rozegrania
    depth1 = 3  # Głębokość wyszukiwania dla gracza 1
    depth2 = 5  # Głębokość wyszukiwania dla gracza 2
    
    # Symulacje dla probabilistycznej wersji ClumsyConnectFour
    results_prob_1 = run_games_with_probabilistic_clumsy(depth1, depth1, True, num_games)
    results_prob_2 = run_games_with_probabilistic_clumsy(depth2, depth2, True, num_games)
    
    # Symulacje dla deterministycznej wersji ConnectFour
    results_det_1 = run_games_with_probabilistic_clumsy(depth1, depth1, False, num_games)
    results_det_2 = run_games_with_probabilistic_clumsy(depth2, depth2, False, num_games)

    # Wyświetlenie wyników dla probabilistycznej gry dla dwóch różnych głębokości
    print(f"⚙️  Symulacja {num_games} gier w ClumsyConnectFour z probabilistycznym przesuwaniem.")
    print(f"Gracz 1: Negamax({depth1}) vs Gracz 2: Negamax({depth1})")
    print(f"📊 Wyniki:")
    print(f"Gracz 1 wygrał: {results_prob_1[1]} razy")
    print(f"Gracz 2 wygrał: {results_prob_1[2]} razy")
    print(f"Remisy: {results_prob_1['draw']}")
    print("\n📈 Podsumowanie:")
    print(f"Zwycięstwa Gracza 1: {results_prob_1[1] / num_games * 100:.1f}%")
    print(f"Zwycięstwa Gracza 2: {results_prob_1[2] / num_games * 100:.1f}%")
    print(f"Remisy: {results_prob_1['draw'] / num_games * 100:.1f}%")

    print(f"\nGracz 1: Negamax({depth2}) vs Gracz 2: Negamax({depth2})")
    print(f"📊 Wyniki:")
    print(f"Gracz 1 wygrał: {results_prob_2[1]} razy")
    print(f"Gracz 2 wygrał: {results_prob_2[2]} razy")
    print(f"Remisy: {results_prob_2['draw']}")
    print("\n📈 Podsumowanie:")
    print(f"Zwycięstwa Gracza 1: {results_prob_2[1] / num_games * 100:.1f}%")
    print(f"Zwycięstwa Gracza 2: {results_prob_2[2] / num_games * 100:.1f}%")
    print(f"Remisy: {results_prob_2['draw'] / num_games * 100:.1f}%")

    # Wyświetlenie wyników dla deterministycznej gry dla dwóch różnych głębokości
    print(f"\n⚙️  Symulacja {num_games} gier w deterministycznej wersji ConnectFour.")
    print(f"Gracz 1: Negamax({depth1}) vs Gracz 2: Negamax({depth1})")
    print(f"📊 Wyniki:")
    print(f"Gracz 1 wygrał: {results_det_1[1]} razy")
    print(f"Gracz 2 wygrał: {results_det_1[2]} razy")
    print(f"Remisy: {results_det_1['draw']}")
    print("\n📈 Podsumowanie:")
    print(f"Zwycięstwa Gracza 1: {results_det_1[1] / num_games * 100:.1f}%")
    print(f"Zwycięstwa Gracza 2: {results_det_1[2] / num_games * 100:.1f}%")
    print(f"Remisy: {results_det_1['draw'] / num_games * 100:.1f}%")

    print(f"\nGracz 1: Negamax({depth2}) vs Gracz 2: Negamax({depth2})")
    print(f"📊 Wyniki:")
    print(f"Gracz 1 wygrał: {results_det_2[1]} razy")
    print(f"Gracz 2 wygrał: {results_det_2[2]} razy")
    print(f"Remisy: {results_det_2['draw']}")
    print("\n📈 Podsumowanie:")
    print(f"Zwycięstwa Gracza 1: {results_det_2[1] / num_games * 100:.1f}%")
    print(f"Zwycięstwa Gracza 2: {results_det_2[2] / num_games * 100:.1f}%")
    print(f"Remisy: {results_det_2['draw'] / num_games * 100:.1f}%")