
import os


def play_round(dealer, player, _min=1, _max=10):

    # Show the player their balance and prompt the player for their bet
    os.system('clear')
    print('Betting Rules: Min =', _min, '|| Max =', _max)
    display_separator()
    print(player.name, '|| Balance = $' + str(player.balance))
    display_separator()
    print('Enter your bet:')
    first_pass = True
    while not (_min <= int(player.bet) <= _max):
        if not first_pass:
            print('Invalid bet!')
        player.bet = int(input())
        first_pass = False
    player.balance -= player.bet

    # Deal initial hands
    dealer.deal_to_self(2)
    dealer.deal_to_player(player, 2)

    # Loop until the player completes their turn
    choice = 0
    while player.score() < 21 and choice != 1:

        # Display cards
        display(dealer, player, dealer_hidden=True)

        # Display player options
        print('Select an option below:')
        print('[1] Stay || [2] Hit\n')

        # Collect player input
        choice = int(input())

        if choice == 2:
            dealer.deal_to_player(player, 1)

    # Loop until the dealer completes their turn
    while dealer.score() < 17 and player.score() <= 21:
        dealer.deal_to_self(1)

    # Display cards
    display(dealer, player)

    # Determine outcome and update the player's balance
    outcome = 0
    blackjack = False
    if player.score() > 21:
        outcome = 2
        print('Player busted.\n')
    elif dealer.score() > 21:
        outcome = 1
        print('Dealer busted!\n')
    elif player.score() > dealer.score() and player.score() == 21 and len(player.hand):
        outcome = 1
        print('Blackjack! Player wins!\n')
    elif player.score() > dealer.score():
        outcome = 1
        print('Player wins!\n')
    elif dealer.score() > player.score():
        outcome = 2
        print('Dealer wins.\n')
    else:
        outcome = 3
        print('Push.\n')

    # Update the player's balance
    if outcome == 1:
        print('Player wins $' + str(player.bet) + '!\n')
        player.balance += 2*player.bet
    elif outcome == 3:
        print('Bet returned to player.\n')
        player.balance += player.bet
    else:
        print('Player loses $' + str(player.bet) + '.\n')
    player.bet = 0

    # Send cards to the trash pile
    trash_player_hand(dealer, player)
    trash_dealer_hand(dealer)


def display_separator(n=50):
    for i in range(0, n):
        print('-', end='')
    print()


def display(dealer, player, dealer_hidden=False):
    os.system('clear')
    if dealer_hidden:
        print('Dealer || Score = ?')
        dealer.print(hidden=True)
    else:
        print('Dealer || Score =', dealer.score())
        dealer.print()
    print(player.name, '|| Score =', player.score(), '|| Bet = $' + str(player.bet))
    player.print()


def trash_dealer_hand(dealer):
    for i in range(0, len(dealer.hand)):
        dealer.trash.append(dealer.hand[0])
        del dealer.hand[0]


def trash_player_hand(dealer, player):
    for i in range(0, len(player.hand)):
        dealer.trash.append(player.hand[0])
        del player.hand[0]