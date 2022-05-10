import random
from card import Card

class Dealer:
    
    def __init__(self):
        self.cards = []
        self.still_playing = True
        self.score = 300
        self.card = Card() 
        

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
        elif self.userGuess == "H" and self.cards[0] < self.cards[1] or self.userGuess == "L" and self.cards[0] > self.cards[1]:
            self.score += 100
        elif self.userGuess == "L" and self.cards[0] < self.cards[1] or self.userGuess == "H" and self.cards[0] > self.cards[1]:
            self.score -= 75  

    def do_outputs(self):
        """Displays the first card, call get_inputs, display the second card and the score.
        Args: self(Dealer)": An instance of Dealer.
        """
        for i in range(2):
            self.cards.append(self.card.draw())
        print(self.cards)

# dealer = Dealer()
# dealer.do_outputs()

# dealer = Dealer()