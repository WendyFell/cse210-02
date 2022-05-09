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
        self.value = 0
        
    def draw(self):
        """Generates a new random value.
        
        Args:
            self (Card): An instance of Die.
        """
        self.value = random.randint(1, 13)
        
# this is a test
        
        