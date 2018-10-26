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
        self.shuffle()
        for i in range(num):
            hand.add_card(self.pop_card())


    def give(self, card, hand):
        self.cards.remove(card)
        hand.add_card(card)

    # Deal as many hands as needed
    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't continue deal. Out of cards!")


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
    hands = []
    hand1 = Hand('North')
    hands.append(hand1)
    hand2 = Hand('South')
    hands.append(hand2)
    hand3 = Hand('East')
    hands.append(hand3)
    hand4 = Hand('West')
    hands.append(hand4)
    # deck.move_cards(hand1, 13)

    deck.deal(hands, 13)
    print()
    hand1.sort()
    print(hand1.name,'\n\n', hand1)

    # deck.move_cards(hand2, 13)
    print()
    hand2.sort()
    print(hand2.name,'\n\n',hand2)

    # deck.move_cards(hand3, 13)
    print()
    hand3.sort()
    print(hand3.name , '\n\n',hand3)

    # deck.move_cards(hand4, 13)
    print()
    hand4.sort()
    print(hand4.name, '\n\n', hand4)

    print()
    print("New thing")

    hand1.move_cards(hand2, 2)
    print(hand1)
    print()
    print(hand2)







if __name__ == '__main__':
    main()