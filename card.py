
class Card:
    def __init__(self, rank, suit, value):
        self.visible = False
        self.rank = rank
        self.suit = suit
        self.value = value
        self.name = self.rank + self.suit
