
from human import Human 
from ai import AI
from player import Player

human_1 = Human()
human_2 = Human()

class Game:

   def __init__(self):
    self.rules = ""
   
   def run_game(self):

      player_number = self.display_welcome()
      self.play_game(player_number)
      self.win_game()

   def display_welcome(self):
      number_of_players = input('''Welcome to Rock Paper Scissors Spock! How many players would you like to have? (single/multi). 
      We're playing best out of three, so first to two wins!''')
      print(f"{self.rules}")
      return number_of_players


   def play_game(self, number_of_players):
      
      if number_of_players == "single":
         self.human.make_choice
         human_1_wins = self.human_1.wins
         human_2_wins = self.huamn_2.wins

         while human_1_wins < 2 or human_2_wins < 2:
            pass



      elif number_of_players == "multi":
         self.ai.make_choice
         human_wins = self.human.wins
         ai_wins = self.ai.wins
         
         while human_wins < 2 or ai_wins < 2:
            pass

      else: 
         print("I'm sorry, I didn't understand that message!")
      
      self.ai.wins

      

   def win_game(self):
      pass