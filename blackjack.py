
import os


def play_round(dealer, player, min_bet=10, max_bet=100):

    # Show the player their balance and prompt the player for their bet
    while not (min_bet <= int(player.bet) <= max_bet):
        os.system('clear')
        print('Betting Rules: Min =', min_bet, '|| Max =', max_bet)
        display_separator()
        print(player.name, '|| Balance = $' + str(player.balance))
        display_separator()
        try:
            player.bet = int(input('Enter your bet:\n'))
        except ValueError:
            player.bet = 0
    player.balance -= player.bet

    # Deal initial hands
    dealer.deal_to_self(2)
    dealer.deal_to_player(player, 2)

    # Loop until the player completes their turn
    choice = '0'
    option_to_hit = True
    option_to_double_down = True
    while player.score() < 21 and choice != '1':

        # Display cards
        display(dealer, player, dealer_hidden=True)

        # Display player options
        print('Select an option below:')
        string = '[1] Stay'
        if option_to_hit:
            string += ' || [2] Hit'
        if option_to_double_down:
            string += ' || [3] Double Down'
        print(string)

        # Collect player input
        choice = input()

        if choice == '2':
            dealer.deal_to_player(player, 1)

        if choice == '3' and option_to_double_down:
            dealer.deal_to_player(player, 1)
            player.balance -= player.bet
            player.bet *= 2
            option_to_hit = False
            option_to_double_down = False

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
    elif player.score() > dealer.score() and player.score() == 21 and len(player.hand) == 2:
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

    # Wait for player to continue
    print('Number of Cards in the Trash =', len(dealer.trash))
    input('Press ENTER to continue:\n')


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
