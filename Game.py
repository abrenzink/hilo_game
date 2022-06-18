from Card import Card
from Player import Player

class Game:
    def __init__(self):
        self.previous = 0
        self.current = 0
        self.is_playing = True
        self.score = 0
        self.total_score = 0

    def get_inputs(self):
        draw_card = input("Draw another card? [y/n] ")
        self.is_playing = (draw_card == "y")

    def do_updates(self):
        if not self.is_playing:
            return

        player = Player()
        answer = input(f"Do you bet next drawn card will be higher than {self.previous}? [y/n] ")
        player.guess = (answer == "y")

        card = Card()
        card.draw()
        self.current = card.value

        result = self.compair_cards()
        self.score = 100 if result == player.guess else -75

        self.total_score += self.score

    def do_outputs(self):
    
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

        while self.is_playing:

            if self.previous == 0:
                card = Card()
                card.draw()
                self.previous = card.value

            self.get_inputs()
            self.do_updates()
            self.do_outputs()

        print(f"Sorry, the game is over. Final score: {self.total_score}\n")

