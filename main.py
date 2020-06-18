
import os

from deck import Deck
from dealer import Dealer
from player import Player
import blackjack as blj

# Create and shuffle the deck
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['♠', '♣', '♡', '♢']
values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
GameDeck = Deck(ranks, suits, values)
GameDeck.shuffle()

# Test - Print the deck
print('Deck Test')
GameDeck.print()

# Initialize dealer and player objects
TheDealer = Dealer(GameDeck)
os.system('clear')
print('What is your name?')
initial_balance = 1000
Player1_name = input()
Player1 = Player(Player1_name, initial_balance)

while Player1.balance > 0:
    blj.play_round(TheDealer, Player1)
    print('Select an option below:')
    print('[0] Quit || [1] Continue')
    choice = ' '
    while choice != '0' and choice != '1':
        choice = input()
    if choice == '0':
        break

print('\nGamer over.')
print('Initial Balance = $' + str(initial_balance))
print('Closing Balance = $' + str(Player1.balance))
print('Thank you for playing! :)')
