
class Card:
    def __init__(self, _rank, _suit, _value):
        self.visible = False
        self.rank = _rank
        self.suit = _suit
        self.value = _value
        self.name = self.rank + self.suit
