from Card import Card

class Game:
    """The instance that controls the game. 
    
    Responsibility: to control the sequence of play.

    Attributes:
        previous(int): Value of the previous drawn card.
        current(int): Value of the current drawn card.
        is_playing (bolean): Defines of the game will keep running.
        score(int): The score for one round of play.
        total_score (int): The score for the entire game.
    """
    def __init__(self):
        """Constructs a new Game.
        
        Args:
            self (Game): an instance of Game.
        """
        self.previous = 0
        self.current = 0
        self.bet = False
        self.is_playing = True
        self.score = 0
        self.total_score = 0

    def get_inputs(self):
        """Ask the user if they want to draw a new card.

        Args:
            self (Game): An instance of Game.
        """
        draw_card = input("Draw another card? [y/n] ")
        self.is_playing = (draw_card == "y")

        answer = input(f"Do you bet next drawn card will be higher than {self.previous}? [y/n] ")
        self.bet = (answer == "y")

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Game): An instance of Game.
        """

        card = Card()
        card.draw()
        self.current = card.value

        result = self.compair_cards()
        self.score = 100 if result == self.bet else -75

        self.total_score += self.score

    def do_outputs(self):
        """Displays the cards and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
    
        print(f"Previous card: {self.previous}")
        print(f"Drawn card: {self.current}")
        print(f"Your total score is: {self.total_score}\n")

        self.previous = self.current

        self.is_playing == (self.total_score < 0)

        if not self.is_playing:
            self.play_game()

    def compair_cards(self):
        if self.current > self.previous:
            return True
        else:
            return False

    def play_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Game): an instance of Game.
        """

        while self.is_playing:

            if self.previous == 0:
                card = Card()
                card.draw()
                self.previous = card.value

            self.get_inputs()
            self.do_updates()
            self.do_outputs()

        print(f"Sorry, the game is over. Final score: {self.total_score}\n")

