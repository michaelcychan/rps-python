import unittest

from src.rps_match import rps_match

class TestRPS(unittest.TestCase):
    def test_rps_match_rock_scissors(self):
        assert rps_match("rock", "scissors") == "rock"

    def test_rps_match_scissors_paper(self):
        assert rps_match("scissors", "paper") == "scissors"

    def test_rps_match_paper_scissors(self):
        assert rps_match("paper", "scissors") == "scissors"

    def test_rps_match_tie(self):
        assert rps_match("scissors", "scissors") == "tie"

    def test_rps_match_wrong_input(self):
        with self.assertRaises(ValueError):
            rps_match("worm", "rock")
    
    