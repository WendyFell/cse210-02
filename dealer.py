from card import Card

class Dealer:
    
    def __init__(self):
        self.cards = []
        self.still_playing = True
        self.score = 300
        self.userGuess = ""
        self.card = Card()

    def start_game(self):
        """Start the game by running the main game loop
        Args: self(Dealer): An instance of Dealer
        """
        while self.still_playing:
            self.get_cards()
            self.get_inputs()
            self.do_updates()
            self.do_outputs()                       
            self.play_again()

    def get_inputs(self):
        """Ask user for a guess of higher or lower.
        Args: self(Dealer)": An instance of Dealer.
        """
        self.userGuess = input("Guess if the next card will be higher or lower (H or L): ")
        self.userGuess = self.userGuess.upper()
        while self.userGuess != "H" and self.userGuess != "L":
            print("Please enter a valid choice (H or L)")
            self.get_inputs()        
            break
        
    def do_updates(self):
        """Updates the score.
         Args: self(Dealer)": An instance of Dealer.
        """        
        if not self.still_playing:
            return
        if self.userGuess == "H" and self.cards[0] < self.cards[1] or self.userGuess == "L" and self.cards[0] > self.cards[1]:
            self.score += 100
        else:
            self.score -= 75         
        
    def get_cards(self):
        """Displays the first card, call get_inputs, display the second card and the score.
        Args: self(Dealer)": An instance of Dealer.
        """
        if len(self.cards) > 1: 
            self.cards.pop(0)
            self.cards.append(self.card.draw())
        else:
            for i in range(2):
                self.cards.append(self.card.draw())
        print(f"Your Card is: {self.cards[0]}")
        
    def do_outputs(self):
        """ Display the score.
        Args: self(Dealer)": An instance of Dealer.
        """
        print(f"Your next card was: {self.cards[1]}")
        while self.still_playing == (self.score <=0):
            print("Game over!")
            break
        else:
            print(f"Your score is {self.score}")
            
            self.still_playing == (self.score > 0)        
    
    def play_again(self):
        """Ask the user if they want to draw another card.

        Args:
            self (Dealer): An instance of Dealer.
        """
        while self.score <= 0:
            self.still_playing = False
            break
            
        else:
            
            willingness = input("Would you like to draw another card? (Y or N) ")
            willingness = willingness.lower()
            self.still_playing = (willingness == "y")
            if willingness == "n":
                print("Thanks for playing!")
            if willingness != "y" and willingness !="n":
                    
                print("Please enter a valid choice (Y or N)")
                self.play_again()
