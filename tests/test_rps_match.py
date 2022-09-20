import unittest
from unittest.mock import Mock

from src.rps_match import rps_match

class TestRPS(unittest.TestCase):
    def test_rps_match_rock_scissors(self):
        player1 = Mock()
        player1.show_roll.return_value = "rock"
        player1.show_name.return_value = "John"
        player2 = Mock()
        player2.show_roll.return_value = "scissors"
        player2.show_name.return_value = "Mary"
        assert rps_match(player1, player2) == "John"

    def test_rps_match_scissors_paper(self):
        player1 = Mock()
        player1.show_roll.return_value = "scissors"
        player1.show_name.return_value = "John"
        player2 = Mock()
        player2.show_roll.return_value = "paper"
        player2.show_name.return_value = "Mary"
        assert rps_match(player1, player2) == "John"

    def test_rps_match_paper_scissors(self):
        player1 = Mock()
        player1.show_roll.return_value = "paper"
        player1.show_name.return_value = "John"
        player2 = Mock()
        player2.show_roll.return_value = "scissors"
        player2.show_name.return_value = "Mary"
        assert rps_match(player1, player2) == "Mary"

    def test_rps_match_tie(self):
        player1 = Mock()
        player1.show_roll.return_value = "scissors"
        player1.show_name.return_value = "John"
        player2 = Mock()
        player2.show_roll.return_value = "scissors"
        player2.show_name.return_value = "Mary"
        assert rps_match(player1, player2) == "tie"

    def test_rps_match_wrong_input(self):
        player1 = Mock()
        player1.show_roll.return_value = "worm"
        player1.show_name.return_value = "John"
        player2 = Mock()
        player2.show_roll.return_value = "scissors"
        player2.show_name.return_value = "Mary"
        with self.assertRaises(ValueError):
            rps_match(player1, player2)
    
    