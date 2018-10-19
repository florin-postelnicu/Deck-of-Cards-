# Deck-of-Cards
In this folder we will build a Standard Deck of Cards using classes

cards1.py : class attributes, suit, and ranks

          class Card(object) constructor method __init__(self)
          class Card(object) readable printing method __str__(self)
          
cards2.py : Added to class Card a new method to compare any two cards
           __cmp__(self, other)
           
           This function creates a readable version of the comparison 
           between any two cards in the deck:
           def print-nice(card1,card2)
           The function is defined outside of the class.
           
cards3.py : Create a new class, the deck of 52 cards.
            class Deck(object) constructor method  __init__(self)
            class Deck(object)                     __str__(self)
            
cards4.py : Adding more VENEER methods( based on predefined functions fro lists)
            To deal cards, we would like a method that removes a card from the deck and returns it.
            
            class Deck(object) pop_card(self)
            
            Since pop removes the last card in the list, we are dealing from the bottom of the deck.
            In real life bottom dealing is frowned upon1, but in this context it’s ok.
            To add a card, we can use the list method append:
            
            class Deck(object) add_card(self, card)
            
            As another example, we can write a Deck method named shuffle using the function shuffle from the random module:
            
            class Deck(object)  shuffle(self)
            
 cards5.py : The new method added is sorting in ascending order the deck of cards.
 
            Since it is not possible to use the sort method from lists, because the comparisons predifined 
            in lists <, >, = do not exist in the context of the Deck clas, I have used :
            
            Card.__cmp__(card1, card2)
            
            that is created inside Card class. The sorting algorithm in this procedure it is Bubble Sort.
 
           
 
           
           
