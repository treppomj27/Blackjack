
import numpy as np

from card import Card


class Deck:
    def __init__(self, _ranks, _suits, _values):
        self.cards = []
        for i in range(0, len(_ranks)):
            for j in range(0, len(_suits)):
                self.cards.append(Card(_ranks[i], _suits[j], _values[i]))

    def print(self):
        string = ' '
        for i in range(0, len(self.cards)):
            string += self.cards[i].name + '  ' if len(self.cards[i].name) == 3 else ' ' + self.cards[i].name + '  '
            if (i + 1) % 13 == 0 and i != len(self.cards) - 1:
                string += '\n '
        print(string, '\n')

    def shuffle(self):
        for i in range(0, len(self.cards)):
            rng = np.random.randint(i, len(self.cards))
            temp = self.cards[i]
            self.cards[i] = self.cards[rng]
            self.cards[rng] = temp
