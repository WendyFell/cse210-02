import random
from card import Card

class Dealer:
    
    def __init__(self):
        self.cards = []
        self.still_playing = True
        self.score = 300
        card = Card() 
        card.draw()

    def start_game(self):
        """Start the game by running the main game loop
        Args: self(Dealer): An instance of Dealer
        """
        while self.still_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask user for a guess of higher or lower.
        Args: self(Dealer)": An instance of Dealer.
        """
        userGuess = input("Guess higher or lower(H or L): ")
        return userGuess
        
    def do_updates(self):
        """Updates the score.
        """
        if not self.still_playing:
            return
        # if self.userGuess == "H" and self.card_drawn > self.card_drawn:

    def do_outputs(self):
        """Displays the first card, call get_inputs, display the second card and the score.
        Args: self(Dealer)": An instance of Dealer.
        """
        



# dealer = Dealer()