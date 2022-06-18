from Card import Card
from Player import Player

class Game:
    def __init__(self):
        self.cards = []
        self.previous = 0
        self.current = 0
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        for i in range(13):
            card = Card();
            self.cards.append(card);

    def get_inputs(self):
        draw_card = input("Draw another card? [y/n] ")
        self.is_playing = (draw_card == "y")

    def do_updates(self):
        if not self.is_playing:
            return

        player = Player()
        player.guess = input("The next drawn card will be higher or lower? [h/l] ")

        card = Card()
        card.draw()
        self.current = card.value
        if (self.current > self.previous) else 

        self.score += card.points 
        self.total_score += self.score

        self.previous = self.current

    def do_outputs(self):
   
        if not self.is_playing:
            return

        print(f"Drawn card: {self.current}\n")
        print(f"Previous card: {self.previous}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)

    def play_game(self):

        if self.previous == 0:
            card = Card()
            card.draw()
            self.previous = card.value

        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

