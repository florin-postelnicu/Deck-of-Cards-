import random


def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
        input("\nPress enter to continue. ")
        print()
    except SyntaxError:
        pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck = []
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    deck.remove('Q\u2663')  # remove a queen as the game requires
    return deck


def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck
    '''
    random.shuffle(deck)


#####################################

def deal_cards(deck):
    '''(list of str)-> tuple of (list of str,list of str)
    Returns two lists representing two decks that are obtained
    after the dealer deals the cards from the given deck.
    The first list represents dealer's i.e. computer's deck
    and the second represents the other player's i.e user's list.
    '''
    dealer = []
    other = []

    variable = 1
    for i in range(len(deck)):
        if variable == 0:
            dealer.append(deck[i])
            variable = 1
        elif variable == 1:
            other.append(deck[i])
            variable = 0

    return (dealer, other)


def remove_pairs(l):
    '''
     (list of str)->list of str
     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled
     Precondition: elements of l are cards represented as strings described above
     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs = []

    if len(l) < 2:
        return l
    l.sort()
    l.append([''])
    item = 1
    while item < len(l):
        if l[item - 1][:-1] != l[item][:-1]:
            no_pairs.append(l[item - 1])
            item += 1
        else:
            item += 2

    random.shuffle(no_pairs)
    return no_pairs


def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    print('')
    print(' '.join(deck))
    print('')


def get_valid_input(n):
    '''
    (int)->int
    Returns an integer given by the user that is at least 1 and at most n.
    Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]

    Precondition: n>=1
    '''
    x = int(input('Give me an integer between 1 and' + ' ' + str(n) + ': '))
    if n >= x >= 1:
        return x
    else:
        while True:
            x = int(input('Invalid number. Please enter integer between 1 and' + ' ' + str(n) + ': '))
            if n >= x >= 1:
                return x
            else:
                continue


def play_game():
    '''()->None
    The function that plays the game.'''

    deck = make_deck()
    shuffle_deck(deck)
    tmp = deal_cards(deck)

    dealer = tmp[0]
    human = tmp[1]

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:")
    print_deck(human)
    print("Do not worry. I cannot see the order of your cards")

    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()

    dealer = remove_pairs(dealer)
    human = remove_pairs(human)
    turn = 0

    while 1 >= turn >= 0:
        if len(human) == 0:
            print('*********************************************************')
            print('Ups. You do not have any more cards')
            print('Congratulations! You, Human, win')
            break
        elif len(dealer) == 0:
            print('*********************************************************')
            print('Ups. I do not have any more cards')
            print('You lost! I, Robot, win')
            break
        else:
            if turn == 0:
                print('*********************************************************')
                print('Your turn.')
                print('')
                print('Your current deck of cards is:')
                print_deck(human)
                n = len(dealer)
                print('I have', n, 'cards. If 1 stands for my first card and\n' + str(n),
                      'for my last card, which of my cards would you like?')
                result = get_valid_input(n)

                if result == 1:
                    print('You asked for my 1st card.')
                elif result == 2:
                    print('You asked for my 2nd card.')
                elif result == 3:
                    print('You asked for my 3rd card.')
                else:
                    print('You asked for my', str(result) + 'th card.')

                print('Here it is. It is', dealer[int(result) - 1])
                print('')
                print('With', dealer[int(result) - 1], 'added, your current deck of cards is:')
                human.append(dealer[int(result) - 1])
                dealer.remove(dealer[int(result) - 1])
                print_deck(human)
                print('And after discarding pairs and shuffling, your deck is:')
                human = remove_pairs(human)
                print_deck(human)
                turn = 1
                wait_for_player()
            elif turn == 1:
                print('*********************************************************')
                print('My turn.')
                print('')
                n = len(human)
                result = random.randint(1, n)

                if result == 1:
                    print('I took your 1st card.')
                elif result == 2:
                    print('I took your 2nd card.')
                elif result == 3:
                    print('I took your 3rd card.')
                else:
                    print('I took your', str(result) + 'th card.')

                dealer.append(human[int(result) - 1])
                human.remove(human[int(result) - 1])
                dealer = remove_pairs(dealer)
                turn = 0
                wait_for_player()


# main
play_game()