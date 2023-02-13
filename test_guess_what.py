import unittest
import guess_what

class TestCheckGuess(unittest.TestCase):
    def test_guesses(self):
        self.assertEqual(guess_what.check_guess(12, 12), 'equal')
        self.assertEqual(guess_what.check_guess(12, 10), 'under')
        self.assertEqual(guess_what.check_guess(12, 14), 'over')

class TestGetBounds(unittest.TestCase):
    def test_lvls(self):
        self.assertEqual(guess_what.get_bounds(1), (1, 20))
        self.assertEqual(guess_what.get_bounds(2), (1, 50))
        self.assertEqual(guess_what.get_bounds(3), (1, 100))
class TestScoreboard(unittest.TestCase):
    def setUp(self) -> None:
        self.scoreboard = guess_what.init_scoreboard()
        guess_what.log_game(self.scoreboard, 1, 12)
        guess_what.log_game(self.scoreboard, 1, 1)
        guess_what.log_game(self.scoreboard, 1, 2)
        guess_what.log_game(self.scoreboard, 2, 3)
        guess_what.log_game(self.scoreboard, 3, 5)
    def test_log_game(self):
        self.assertEqual(self.scoreboard, {1: [12, 1, 2], 2: [3], 3: [5]})
    def test_get_rows(self):
        self.assertEqual(guess_what.scoreboard_get_rows(self.scoreboard), [[12, 3, 5], [1, 0, 0], [2, 0, 0]])
        guess_what.log_game(self.scoreboard, 2, 3)
        self.assertEqual(guess_what.scoreboard_get_rows(self.scoreboard), [[12, 3, 5], [1, 3, 0], [2, 0, 0]])
        guess_what.log_game(self.scoreboard, 2, 3)
        guess_what.log_game(self.scoreboard, 2, 3)
        self.assertEqual(guess_what.scoreboard_get_rows(self.scoreboard), [[12, 3, 5], [1, 3, 0], [2, 3, 0], [0, 3, 0]])