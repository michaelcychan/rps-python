class Player:

    def __init__(self, name):
        self.name = name
        self._roll = None

    def roll(self, roll):
        self._roll = roll

    def show_roll(self):
        return self._roll
