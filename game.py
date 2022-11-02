
from human import Human 
from ai import AI
from player import Player
from time import sleep

human_1 = Human()
human_2 = Human()
ai_1 = AI()

class Game:

   def __init__(self):
    
    self.rules = '''
Scissors cuts Paper 
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock'''
     

   def run_game(self):

      player_number = self.display_welcome()
      self.play_game(player_number)
      self.win_game()

   def display_welcome(self):
    print('\nWelcome to Rock Paper Scissors Spock!\n')
    sleep(1)
    number_of_players = input('''\nHow many players would you like to have? (single/multi). 
    We're playing best out of three, so first to two wins!\n''')
    sleep(1)
    print(f"{self.rules}")
    sleep(1)
    return number_of_players


   def play_game(self, number_of_players):
      
      if number_of_players == "single":
        while human_1.wins < 2 or human_2.wins < 2:
         self.human.make_choice
        #  human_1_wins = self.human_1.wins
        #  human_2_wins = self.huamn_2.wins

         
        pass



      elif number_of_players == "multi":
        while human_1.wins < 2 or ai_1.wins < 2:
         ai_1.make_choice
        #  human_1.wins = self.human.wins
        #  ai_wins = self.ai.wins
         
         
        pass

      else: 
         print("\nI'm sorry, I didn't understand that message!\n")
    
    
      

   def win_game(self):
      pass