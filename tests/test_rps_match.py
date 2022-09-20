import unittest

from src.rps_match import rps_match

class TestRPS(unittest.TestCase):
    def test_rps_match_rock_scissors(self):
      assert rps_match("rock", "scissors") == "rock"