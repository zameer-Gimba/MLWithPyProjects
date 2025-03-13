import unittest
from RPS_game import play, quincy, abbey, kris, mrugesh  # Import existing bots
from RPS import player  # Import your player function

class TestRPSGame(unittest.TestCase):
    def test_quincy(self):
        """Test player against Quincy bot (repeats 'RPS' pattern)."""
        win_rate = self.get_win_rate(player, quincy)
        self.assertGreaterEqual(win_rate, 0.6, "Failed to defeat Quincy with at least 60% win rate")

    def test_abbey(self):
        """Test player against Abbey bot (uses Markov chain strategy)."""
        win_rate = self.get_win_rate(player, abbey)
        self.assertGreaterEqual(win_rate, 0.6, "Failed to defeat Abbey with at least 60% win rate")

    def test_kris(self):
        """Test player against Kris bot (always plays 'R')."""
        win_rate = self.get_win_rate(player, kris)
        self.assertGreaterEqual(win_rate, 0.6, "Failed to defeat Kris with at least 60% win rate")

    def test_mrugesh(self):
        """Test player against Mrugesh bot (uses frequency-based strategy)."""
        win_rate = self.get_win_rate(player, mrugesh)
        self.assertGreaterEqual(win_rate, 0.6, "Failed to defeat Mrugesh with at least 60% win rate")

    def get_win_rate(self, player1, player2, num_games=1000):
        """Helper function to calculate win rate of player1 against player2."""
        results = play(player1, player2, num_games)
        wins = results['player1_wins']
        return wins / num_games  # Win rate percentage

if __name__ == "__main__":
    unittest.main()
