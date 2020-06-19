
import os
from time import perf_counter

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

# Infinite loop of rounds
start_time = perf_counter()
rounds_played = 0
while Player1.balance > 0:
    blj.play_round(TheDealer, Player1)
    rounds_played += 1
    choice = ' '
    while choice != '0' and choice != '1':
        os.system('clear')
        print(Player1.name, '|| Balance = $' + str(Player1.balance))
        blj.display_separator()
        print('Rounds Played =', rounds_played, '|| Time Elapsed =', int((perf_counter() - start_time)/60), 'min')
        blj.display_separator()
        print('Select an option below:')
        print('[0] Quit || [1] Continue')
        choice = input()
    if choice == '0':
        break

# End of game output
os.system('clear')
print('Gamer Over')
blj.display_separator()
print('Rounds Played =', rounds_played)
print('Time Elapsed =', int((perf_counter() - start_time)/60), 'min')
print('Avg. Time per Round =', round((perf_counter() - start_time)/rounds_played, 1), 's')
blj.display_separator()
print('Initial Balance = $' + str(initial_balance))
print('Closing Balance = $' + str(Player1.balance))
blj.display_separator()
if Player1.balance > initial_balance:
    print('Player won $' + str(Player1.balance - initial_balance) + '.')
elif initial_balance > Player1.balance:
    print('Player lost $' + str(Player1.balance - initial_balance) + '.')
else:
    print('Player broke even.')
blj.display_separator()
print('Thank you for playing! :)')
