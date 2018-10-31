

from cards8 import*


class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()


class FoolHand(Hand):
    def remove_matches(self):
        count = 0
        original_card = self.cards[:]
        for card in original_card:
            match = Card(3-card.suit,card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Hand {}: {} matches {}".format(self.name, card, match))
                count = count+1
def main():
    deck = Deck()
    print(deck)


if __name__=='__main__':
    main()