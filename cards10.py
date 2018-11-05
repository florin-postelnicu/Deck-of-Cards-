from cards9 import*

class FoolGame(CardGame):
    def play(self, names):
        # Remove a card, Ace of Spades
        # The Fool is the Ace of clubs
#         self.deck.remove_card(Card(0, 1))

        # make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(FoolHand(name))

        # deal the cards
        self.deck.deal(self.hands, 52//len(self.hands)+1)
        print("_______________Cards have been dealt")
        self.printHands()

        # remove initial matches
        matches = self.removeAllMatches()
        print("________________Matches have been removed, play begins\n")
        self.printHands()

        # Play until all cards are removed
        turn = 0
        numHands = len(self.hands)
        while matches< 25:
            matches = matches + self.play_one_turn(turn )
            turn = (turn +1)% numHands
        print("________________ game Over")
        self.printHands()


    def removeAllMatches(self):
        count = 0
        for hand in self.hands:
            count = count + hand.remove_matches()
        return count

    def play_one_turn(self, i):
        if self.hands[i]==[]:
            return 0
        neighbor = self.find_neighbor(i)
        pickedCard = self.hands[neighbor].pop_card()
        self.hands[i].add_card(pickedCard)
        print("Hand", self.hands[i], " picked ", pickedCard)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count

    def find_neighbor(self, i):
        numHands = len(self.hands)
        for next in range (1, numHands):
            neighbor = (i + next)% numHands
            if not self.hands[neighbor]==[]:
                return neighbor

    def printHands(self):
        numHands = len(self.hands)
        for i in range(numHands -1):
            print(self.hands[i])



def main():
    game = FoolGame()
    game.play(["Mario","Barbaro","Camaro","Sakura"])


if __name__ == '__main__':
    main()
