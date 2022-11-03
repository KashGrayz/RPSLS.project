#AI(child class)

import random
from player import Player

class AI(Player):

    def __init__(self):

        super().__init__()
        
    def make_choice(self):
        weapon = random.randint(0, 4)
        return weapon
