"""
This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com
Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

More methods for the deck class
Three new methods added to the Deck class.
The VENEER methods are based on the methods for lists:


list.pop()  To deal the last card in the deck
list.append(object) To return a card to the deck
random.shuffle(list) To shuffle the deck

Check if you can add other methods specific to a list , like list.sort()
that will sort ascending a list of numbers(an array)! Explain the result of it!

"""

# Imports should be done at the top of the program

import random

class Card(object):
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=0): # A constructor for instances of Card class
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """ print(Card(0,1)) Ace of Clubs"""
        return '{0} of {1}'.format(Card.rank_names[self.rank], Card.suit_names[self.suit])


    # Comparison method __cmp__
    def __cmp__(self, other):
        # check the suits
        if self.suit > other.suit : return 1
        if self.suit < other.suit : return -1

        # suits are the same , check the ranks
        if self.rank > other.rank : return 1
        if self.rank < other.rank : return -1

        # otherwise, the cards are equal(identical)
        return 0


class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res =[]
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    # To deal cards, we would like a method that removes a card from the deck and returns it.
    # The list method pop provides a convenient way to do that:

    def pop_card(self):
        return self.cards.pop()

    # Since pop removes the last card in the list, we are dealing from the bottom of the deck.
    # In real life bottom dealing is frowned upon1, but in this context it’s ok.
    # To add a card, we can use the list method append:

    def add_card(self, card):
        return self.cards.append(card)

    # A method like this that uses another function without doing much real work is sometimes called a veneer.
    # The metaphor comes from woodworking, where it is common to glue a thin layer of good quality wood
    # to the surface of a cheaper piece of wood.
    #
    # In this case we are defining a “thin” method that expresses a list operation
    #  in terms that are appropriate for decks.
    #
    # As another example, we can write a Deck method named shuffle using the function shuffle from the random module:

    def shuffle(self):
        random.shuffle(self.cards)







def main():
    deck = Deck()
    print(deck)

    Deck.pop_card(deck)
    print(deck)
    Deck.add_card(deck, Card(3,13))
    print(deck)

    # When done experimenting with the pop_card(), and add_card(deck, card) methods
    # try the shuffle(deck) method
    # Deck.shuffle(deck)
    # print(deck)






if __name__ =='__main__':
    main()
