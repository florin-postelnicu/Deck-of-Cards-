"""
This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com
Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html


Check if you can add other methods specific to a list , like list.sort()
that will sort ascending a list of numbers(an array)! Explain the result of this application
to your program!

*********************************************************************************

As a consequence of how the comparison of two cards of the deck is done , through
Card.__cmp__(card1, card2) method,
it is not possible to use the build in sort () function for lists; the symbols < , = ,  >  are not defined in the
 context of the Deck class.
Therefore the sort method inside the Deck class should be built  on  __cmp__ method.

Run several test with the new sort method for the Deck class.
Comment every line of the respective method.
The algorithm used in this method is called bubble sort.
Find bibliography about it. Cite several examples . Understand the mechanism of it.
Maybe write a small project on Bubble Sort Algorithm.

"""

# Imports should be done at the top of the program

import random


class Card(object):
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=0):  # A constructor for instances of Card class
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """ print(Card(0,1)) Ace of Clubs"""
        return '{0} of {1}'.format(Card.rank_names[self.rank], Card.suit_names[self.suit])

    # Comparison method __cmp__
    def __cmp__(self, other):
        # check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1

        # suits are the same , check the ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1

        # otherwise, the cards are equal(identical)
        return 0


class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        return self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    # Using Card class method __cmp__, the next function does the
    # sorting in ascending order of the deck
    # the algorithm used is Bubble Sort.

    def sort(self):
        running = True
        while running:
            switch = 0
            for index in range(len(self.cards) - 1):
                if Card.__cmp__(self.cards[index], self.cards[index + 1]) > 0:
                    change = self.cards[index + 1]
                    self.cards[index + 1] = self.cards[index]
                    self.cards[index] = change
                    switch = 1
                if switch == 1:
                    running = True
                else:

                    return self.cards


def main():
    deck = Deck()
    # print(deck)

    # Deck.shuffle(deck)
    # print(deck)
    Deck.sort(deck)
    print(deck)


if __name__ == '__main__':
    main()