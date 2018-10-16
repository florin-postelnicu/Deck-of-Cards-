'''
Building a Deck

Now that we have Cards, the next step is to define Decks. Since a deck is made up of cards,
it is natural for each Deck to contain a list of cards as an attribute.
The following is a class definition for Deck. The init method creates the attribute cards and
generates the standard set of fifty-two cards.
'''

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
    """
    Represents a deck of cards ,

    Attributes :
       cards: list of cards


    This method demonstrates an efficient way to accumulate a large string: building a list of
strings and then using join. The built-in function str invokes the __str__ method on each
card and returns the string representation.

    """

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




def main():
  deck = Deck()
  print(deck)




if __name__ =='__main__':
    main()