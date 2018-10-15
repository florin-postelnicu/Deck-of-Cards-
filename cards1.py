"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html


Here will define a class Card(object)
with two standard attributes:
suit_names = ['Clubs', 'Diamonds", 'Hearts', 'Spades']
rank_names = [ None, 'Ace', '2', '3', '4','5','6','7','8','9','10', 'Jack', 'Queen', 'King']

Variables like suit_names and rank_names, which are defined inside a class but outside
of any method, are called class attributes because they are associated with the class object
Card.

"""

class Card:
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=0): # A constructor for instances of Card class
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """ print(Card(0,1)) Ace of Clubs"""
        return '{0} of {1}'.format(Card.rank_names[self.rank], Card.suit_names[self.suit])



def main():
    print(Card(0,1))
    # Printing all the cards in the deck
    for suit in range(4):
        for rank in range(1,14):
            print('{0} of {1}'.format(Card.rank_names[rank], Card.suit_names[suit]))





if __name__ =='__main__':
    main()