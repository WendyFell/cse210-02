# cse210-02

Name: HILO card game
Overview:
    Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.
    Rules:
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

Project Structure:
    root                (project root folder)
    +--cse210-02        (source code for game)
        +--dealer       (specific class)
        +--card         (specific class)
        +--__main__.py  (program entry point)
        +--README.md           (general info)

Collaborators: Team 02- 
    Camila Melo-mel19009@byui.edu
    Nelson Tomas Familia Arroyo-fam16002@byui.edu
    Wendy Fellows-fellowswendylynn@gmail.com
    Koko Mouhamed Jean Patrick-mouhamedkoko996@gmail.com
    Aaron Douglass-dou15009@byui.edu

Required Software:
    Visual Studio Code
    GitHub
    Python

The following is a collaboration to start figuring out how to put the game into objects then into classes. It is not a complete list, we added code after we started the classes. The program is set up to have each class with its own file and finally running the program in a __main__.py file.
OBJECTS:
Dealer
    Responsiblity-control game
    Behaviors-  run the game
                ask player to guess
                evaluate guess is correct
                score guess
                ask player if they want to keep playing
    State-      value of guess
                value of the score

Cards
    Responsibility- keep track of which card is drawn
    Behaviors- display card 
    States- card numbers 1-13


CLASSES:
dealer
    methods:
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
            parameters
            return types
cards
    methods-function to draw card
    parameters-value
    return types-random choose number between 1 and 13
