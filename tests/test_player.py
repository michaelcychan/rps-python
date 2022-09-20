import unittest

from src.player import Player

class TestPlayer(unittest.TestCase):
    
    def test_new_player(self):
        player1 = Player("John")
        assert isinstance(player1, Player)
        assert player1.name == "John"

    def test_player_roll(self):
        player1 = Player("John")
        player1.roll("rock")
        assert player1.show_roll() == "rock"