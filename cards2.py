
'''

This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com
Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html


Using a compare method for comparison of two cards

For built-in types, there are conditional operators (<, >, ==, etc.) that compare values and determine when one
is greater than, less than, or equal to another. For user-defined types,
we can override the behavior of the built-in operators by providing a method named __cmp__.

__cmp__ takes two parameters, self and other, and returns a positive number if the first object is greater,
 a negative number if the second object is greater, and 0 if they are equal to each other.

The correct ordering for cards is not obvious.
For example, which is better, the 3 of Clubs or the 2 of Diamonds?
One has a higher rank, but the other has a higher suit. In order to compare cards,
you have to decide whether rank or suit is more important.

The answer might depend on what game you are playing, but to keep things simple,
we’ll make the arbitrary choice that suit is more important, so all of the Spades outrank all of the Diamonds,
and so on.

A second version of the comparison method, using the built in __cmp__ function,
and comparing tuples(pairs of objects)



def __cmp__(self, onother):
    t1 = self.suit, self.rank
    t2 = other.suit, other.rank
    return cmp(t1,t2)

1) Check the method in your program replacing the old one.
2) Work a nice display of the comparison result, like:
Ace of Clubs is a lower card than  Ace of Hearts .... for Card.__cmp__(Card(0,1), Card(2,1))
or,

Ace of Spades is higher than Ace of diamonds,
or,

Ace of Clubs is identical to Ace of Clubs

Suggestion :
You can create a special function outside of the class Card
that prints the friendly messages based on comparison of
the given cards.

'''





class Card:
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

# Put the definitions of functions
def print_nice(card1, card2):
    if Card.__cmp__(card1, card2) == 1:
        return 'Card {0} is higher than Card {1}'.format(card1, card2)
    if Card.__cmp__(card1, card2) == -1:
        return 'Card {0} is lower than Card {1}'.format(card1, card2)
    if Card.__cmp__(card1, card2) == 0:
        return 'Card {0} is identical to  Card {1}'.format(card1, card2)




def main():
    print(Card(0,1))
    # Printing all the cards in the deck
    for suit in range(4):
        for rank in range(1,14):
            print('{0} of {1}'.format(Card.rank_names[rank], Card.suit_names[suit]))

    print(Card.__cmp__(Card(0,1), Card(0,7)))
    
    print(print_nice(Card(0,1), Card(0,7)))
    print(print_nice(Card(2,13), Card(0,1)))
    print(print_nice(Card(0,1), Card(0,1)))





if __name__ =='__main__':
    main()
