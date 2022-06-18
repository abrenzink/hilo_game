import random

class Card:
    """A piece of paper that can have different number from1 to 13.

    The responsibility of Die is to keep track of the card's value.

    Attributes:
        value(int): The number of the card.
    """
    def __init__ (self):
        self.value = 0

    def draw(self):
        """Randomly pics a number from 1 to 13.

        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1,13)
