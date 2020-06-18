
class Player:
    def __init__(self, name, balance):
        self.name = name
        self.hand = []
        self.balance = balance
        self.bet = 0

    # noinspection DuplicatedCode
    def print(self):
        string = ' '
        for i in range(0, len(self.hand)):
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
