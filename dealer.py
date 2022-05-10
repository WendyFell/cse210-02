import random
from card import Card

class Dealer:
    
    def __init__(self):
        self.still_playing = True
        self.score = 0
        card = Card() 
        card.draw()



userGUess = input("Guess higher or lower(H or L): ")

dealer = Dealer()