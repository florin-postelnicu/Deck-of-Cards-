

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
            match = Card(3- card.suit,card.rank)

            for exam in self.cards:
                if Card.__cmp__(exam, match)== 0:
                    # print(count, " exam is :", exam, " Match is :", match)
                    self.cards.remove(card)
                    self.cards.remove(exam)
                    print("Hand {}: {} matches {}".format(self.name, card, match))
                    count+= 1
        return print(count)

def main():
    game = CardGame()
    hand = FoolHand("Dario")
    game.deck.deal([hand], 26)
    print(hand)
    hand.remove_matches()
    print(hand)
    

if __name__=='__main__':
    main()
