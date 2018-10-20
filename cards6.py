'''
This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com
Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html


***************************************************
Create class Hand(Deck)
Inheritance

The language feature most often associated with object-oriented programming is inheritance. Inheritance is the ability
to define a new class that is a modified version of an existing class.

The primary advantage of this feature is that you can add new methods to a class without modifying the existing class.
It is called inheritance because the new class inherits all of the methods of the existing class.
Extending this metaphor, the existing class is sometimes called the parent class.
The new class may be called the child class or sometimes subclass.

Inheritance is a powerful feature. Some programs that would be complicated without inheritance can be written concisely
and simply with it. Also, inheritance can facilitate code reuse, since you can customize the behavior of parent classes
without having to modify them. In some cases, the inheritance structure reflects the natural structure of the problem,
which makes the program easier to understand.

On the other hand, inheritance can make programs difficult to read. When a method is invoked,
it is sometimes not clear where to find its definition. The relevant code may be scattered among several modules.
Also, many of the things that can be done using inheritance can be done as elegantly (or more so) without it.
If the natural structure of the problem does not lend itself to inheritance,
this style of programming can do more harm than good.

One of our goals is to write code that could be reused to implement other card games.
'''


import random


class Card(object):
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """ print(Card(0,1)) Ace of Clubs"""
        return '{0} of {1}'.format(Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __cmp__(self, other):
        # check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1

        # suits are the same , check the ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1

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

    # Removing a card

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def shuffle(self):
        random.shuffle(self.cards)

    # The move_cards method
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


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


class Hand(Deck):

    def __init__(self, name=" "):

        self.cards = []
        self.name = name

    # For just about any card game, it is necessary to add and remove cards from the deck.
    # Removing cards , and Adding cards is already taken care of, since Hand inherits remove from Deck.
    # The only problem with this calss is that the only way to work with it is through the methods
    # in Deck class. If something else is needed, than the Hand class should OVERRIDE the methods
    # conflicting with those in Deck class.

    # Since during a game the transfer of cards it is done between hand and deck, the Deck class
    # would get such a method: move_cards (self, hand, num)

    # Any new methods in the Hand class should be OK



def main():
    deck = Deck()
    deck.shuffle()
    hand1 = Hand('Mario')
    deck.move_cards(hand1, 13)
    print(hand1)





if __name__ == '__main__':
    main()