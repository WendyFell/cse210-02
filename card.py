import random

class Card:
    """A card can have values from 1 to 13.

    The responsibility of Card is to keep track which card is drawn
   
    Attributes:
        value (int): The number of the card.
    """

    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.suits = 0
        self.cards = 0
        
    def draw(self):
        """Generates a new random card and suit.
        
        Args:
            self (Card): An instance of Card.
        """
        self.suits = random.choice(['\u2666', '\u2665', '\u2663', '\u2660'])
        self.cards = random.randint(1, 13)    
        card_drawn = (f"{self.cards} {self.suits}")       
        print(f'{self.cards}{self.suits}')
        return card_drawn

        
        