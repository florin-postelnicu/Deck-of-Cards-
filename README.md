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
            
            
 cards6.py : class Hand is defined as a subclass( child) of Deck. The Deck class has been updated with more methods:
             remove_card(self, card) , and move_cards(self, hand, num). 
             Since Hand is a child of Deck, Hand class inherits all Deck's methods, including the last two. Self could be a hand as well, not only a deck.
 
           The language feature most often associated with object-oriented programming is inheritance.
           Inheritance is the ability to define a new class that is a modified version of an existing class.

           The primary advantage of this feature is that you can add new methods to a class without 
           modifying the existing class.It is called inheritance because the new class inherits all of the methods
           of the  existing class.
           Extending this metaphor, the existing class is sometimes called the parent class.
           The new class may be called the child class or sometimes subclass.

           Inheritance is a powerful feature. Some programs that would be complicated without inheritance can be written     
           concisely and simply with it. 
           Also, inheritance can facilitate code reuse, since you can customize the behavior of parent classes
           without having to modify them. In some cases, the inheritance structure reflects the natural structure of the 
           problem,which makes the program easier to understand.

           On the other hand, inheritance can make programs difficult to read. When a method is invoked,
           it is sometimes not clear where to find its definition. The relevant code may be scattered among several modules.
           Also, many of the things that can be done using inheritance can be done as elegantly (or more so) without it.
           If the natural structure of the problem does not lend itself to inheritance,
           this style of programming can do more harm than good.

          
          One of our goals is to write code that could be reused to implement other card games.
 
           
 
           
           
