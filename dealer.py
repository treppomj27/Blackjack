
class Dealer:
    def __init__(self, deck):
        self.deck = deck
        self.hand = []
        self.trash = []

    def print(self, hidden=False):
        string = ' '
        for i in range(0, len(self.hand)):
            if hidden and i == 0:
                string += '-?-  '
            else:
                string += self.hand[i].name + '  ' if len(self.hand[i].name) == 3 else ' ' + self.hand[i].name + '  '
        print(string, '\n')

    # noinspection DuplicatedCode
    def score(self):
        total_value, aces = 0, 0
        for i in range(0, len(self.hand)):
            total_value += self.hand[i].value
            if self.hand[i].rank == 'A':
                aces += 1
        while total_value > 21 and aces > 0:
            total_value -= 10
            aces -= 1
        return total_value

    def deal_to_self(self, n):
        for i in range(0, n):
            self.hand.append(self.deck.cards[0])
            del self.deck.cards[0]

    def deal_to_player(self, player, n):
        for i in range(0, n):
            player.hand.append(self.deck.cards[0])
            del self.deck.cards[0]
