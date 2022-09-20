import unittest
from unittest.mock import patch
from sys import stderr

from src.game import game

class TestGame(unittest.TestCase):
    @patch('builtins.print')
    def test_new_game(self, capsys):
        captured = capsys.readouterr()
        game()
        assert captured.out == "Welcome to the RPS Game!"
        # assert captured.out == "Please enter name of Player 1:"
        # game.input = lambda: "John"
        # assert captured.out == "Please enter name of Player 2:"
        # game.input = lambda: "Mary"
        # assert captured.out == "It is an RPS game John vs Mary!"