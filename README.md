# cse210-02

Overview
Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.

Rules
Hilo is played according to the following rules.

The player starts the game with 300 points.
Individual cards are represented as a number from 1 to 13.
The current card is displayed.
The player guesses if the next one will be higher or lower.
The the next card is displayed.
The player earns 100 points if they guessed correctly.
The player loses 75 points if they guessed incorrectly.
If a player reaches 0 points the game is over.
If a player has more than 0 points they decide if they want to keep playing.
If a player decides not to play again the game is over.




OBJECTS:
Dealer
    Responsiblity-control game
    Behaviors- show card drawn
            ask player to guess
            evaluate guess is correct
            score guess
    State- value of guess

Cards
    Responsibility- keep track of which card is drawn
    Behaviors- display card 
    States- card numbers 1-13


CLASSES:
dealer
    methods-
    parameters
    return types
cards
    methods-function to draw card
    parameters-value
    return types-random choose number between 1 and 13

Need to draw a card-function in dealer class
Need to ask player to guess higher or lower-input with variable in dealer class
Need to draw another card-function in dealer class
Evaluate if guess is true or false-function in dealer
Score guess-function in dealer
Ask player to play again-input with variable in dealer class


METHODS:
__init__(self)
    attributes:
        is_playing
        score
        total_score
        cards

start_game(self): Starts the game by running a loop.
    Return: None

play_again(self): Get an input from player if he wants to play again
    return: start game if yes

display_card(self):
    return 

guess=
    gets an input of higher or lower

evaluate_guess(self):
    looks at display_card before and after guess
    if guess is correct points added
    else points deducted
    return score