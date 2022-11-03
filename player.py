#Player (parent class)

class Player:

    def __init__(self):
        self.name = ''
        self.wins = 0
        self.moves_list = []
        #list to display before each play
        self.move_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

        #determines winner of each round
    def make_choice(self):
        weapon = input(f"{self.name}, please choose a weapon.\n")
        return weapon
      
    