
from human import Human 
from ai import AI
from player import Player
from time import sleep

from playsound import playsound

human_1 = Human()
human_2 = Human()
human_1.name = "Player 1"
human_2.name = "Player 2"
ai_1 = AI()
ai_1.name = "Computer"


class Game:

   def __init__(self):
    
    self.rules = '''
    Rock crushes Scissors
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
      winner = self.play_game(player_number)
      answer = self.win_game(winner)
      while answer == "y":
         winner = self.play_game(player_number)
         answer = self.win_game(winner)
      print("\nThanks for playing!\n")


   def display_welcome(self):

      print('\nWelcome to Rock Paper Scissors Lizard Spock!\n')
      sleep(1)
      number_of_players = input('\nHow would you like to play? (single/multi).\n')
      sleep(1)
      print(f"{self.rules}")
      sleep(1)
      print("\nWe're playing best out of three, so first to two wins!\n")
      return number_of_players


   def play_game(self, number_of_players):
      
      if number_of_players == "multi":
         choice = ""
         choice1 = ""
         
         while human_1.wins or human_2.wins < 2:
            choice = human_1.make_choice()
            print('\n')
            while choice not in human_1.move_list:
               print("I'm sorry, I didn't understand that message!")
               choice = human_1.make_choice()

            print(f'''\n{human_2.name} - no peeking!\n









            ''')
            choice1 = human_2.make_choice()
            while choice not in human_2.move_list:
               print("I'm sorry, I didn't understand that message!")
               choice = human_2.make_choice()

            if choice == choice1:
               print(f'You both choose {choice1}')
               print("It's a tie!")

            ## Human 1 Wins

                  #Rock vs Scissors or Lizard
            elif choice == human_1.move_list[0]:
               if choice1 == human_2.move_list[2] or choice1 == human_2.move_list[3]:
                  human_1.wins += 1
                  if choice1 == human_2.move_list[2]:
                     print('\nRock crushes Scissors')
                     print(f'{human_1.name} Wins!')
                  elif choice1 == human_2.move_list[3]:
                     print('\nRock crushes Lizard')
                     print(f'{human_1.name} Wins!')

                  #Paper vs Scissors or Spock     
            elif choice == human_1.move_list[1]:
               if choice1 == human_2.move_list[0] or choice1 == human_2.move_list[4]:
                  human_1.wins += 1
                  if choice1 == human_2.move_list[0]:
                     print('\nScissors cuts Paper')
                     print(f'{human_1.name} Wins!')
                  elif choice1 == human_2.move_list[4]:
                     print('\nSpock smashes Scissors')
                     print(f'{human_1.name} Wins!')

                  #Scissors vs Paper or Lizard
            elif choice == human_1.move_list[2]:
               if choice1 == human_2.move_list[1] or choice1 == human_2.move_list[3]:
                  human_1.wins += 1
                  if choice1 == human_2.move_list[1]:
                     print('\nScissors cuts Paper')
                     print(f'{human_1.name} Wins!')
                  elif choice1 == human_2.move_list[3]:
                     print('\nScissors decapitates Lizard')
                     print(f'{human_1.name} Wins!')
                  
                  #Lizard vs Spock or Paper
            elif choice == human_1.move_list[3]:
               if choice1 == human_2.move_list[4] or choice1 == human_2.move_list[1]:
                  human_1.wins += 1
                  if choice1 == human_2.move_list[4]:
                     print('\nLizard poisons Spock')
                     print(f'{human_1.name} Wins!')
                  elif choice1 == human_2.move_list[1]:
                     print('\nLizard eats Paper')
                     print(f'{human_1.name} Wins!')

                   #Spock vs Scissors or Rock
            elif choice == human_1.move_list[4]:
               if choice1 == human_2.move_list[2] or choice1 == human_2.move_list[0]:
                  human_1.wins += 1
                  if choice1 == human_2.move_list[2]:
                     print('\nSpock smashes Scissors')
                     print(f'{human_1.name} Wins!')
                  elif choice1 == human_2.move_list[0]:
                     print('\nSpock vaporizes Rock')
                     print(f'{human_1.name} Wins!')

            ## Human 2 Wins

                  #Rock vs either Scissors or Lizard
            if choice1 == human_2.move_list[0]:
               if choice == human_1.move_list[2] or choice == human_1.move_list[3]:
                  human_2.wins += 1
                  if choice == human_1.move_list[2]:
                     print('\nRock crushes Scissors')
                     print(f'\n{human_2.name} Wins!')
                  elif choice == human_1.move_list[3]:
                     print('\nRock crushes Lizard')
                     print(f'\n{human_2.name} Wins!')

                  #Paper vs Scissors or Spock
            elif choice1 == human_2.move_list[1]:
               if choice == human_1.move_list[0] or choice == human_1.move_list[4]:
                  human_2.wins += 1
                  if choice == human_1.move_list[0]:
                     print('\nPaper covers Rock')
                     print(f'\n{human_2.name} Wins!')
                  elif choice == human_1.move_list[4]:
                     print('\nPaper disproves Spock')
                     print(f'\n{human_2.name} Wins!')

                  #Scissors vs Paper or Lizard
            elif choice1 == human_2.move_list[2]:
               if choice == human_1.move_list[1] or choice == human_1.move_list[3]:
                  human_2.wins += 1
                  if choice == human_1.move_list[1]:
                     print('\nScissors cuts Paper')
                     print(f'\n{human_2.name} Wins!')
                  elif choice == human_1.move_list[3]:
                     print('\nScissors decapitates Lizard')
                     print(f'\n{human_2.name} Wins!')

                  #Lizard vs Spock or Paper
            elif choice1 == human_2.move_list[3]:
               if choice == human_1.move_list[4] or choice == human_1.move_list[2]:
                  human_2.wins += 1
                  if choice == human_1.move_list[4]:
                     print('\nSpock vaporizes Rock')
                     print(f'\n{human_2.name} Wins!')
                  elif choice == human_1.move_list[2]:
                     print('\nLizard eats Paper')
                     print(f'\n{human_2.name} Wins!')

                  #Spock vs Scissors or Rock
            elif choice1 == human_2.move_list[4]:
               if choice == human_1.move_list[2] or choice == human_1.move_list[0]:
                  human_2.wins += 1
            
            
            else:
               print("I'm sorry, I didn't understand that message!")
        
         winner = ''
         if human_1.wins >= 2:
            winner = human_1.name
            human_1.wins = 0
            human_2.wins = 0
         else:
            winner = human_2.name
            human_1.wins = 0
            human_2.wins = 0
         return winner

                ##Human vs AI Play


      elif number_of_players == "single":

         choice = ""
         choice1 = ""

         while human_1.wins or ai_1.wins < 2:

            choice1 = human_1.make_choice()
            while choice1 not in human_1.move_list:
               print("I'm sorry, I didn't understand that message!")
               choice1 = human_1.make_choice()

            ai_choice = ai_1.make_choice()
            
            
            if ai_1.move_list[ai_choice] == choice1:
               print(f'You both choose {choice1}')
               print("It's a tie!")
               
            ## AI Wins

                  #Rock vs either Scissors or Lizard
            elif ai_1.move_list[ai_choice] == ai_1.move_list[0]:
               if choice1 == human_1.move_list[2] or choice1 == human_1.move_list[3]:
                  ai_1.wins +=1
                  if choice1 == human_1.move_list[2]:
                     print('\n Rock crushes Scissors!\n')
                     print(f'\n{ai_1.name} Wins!!')
                  elif choice1 == human_1.move_list[3]:
                     print('\n Rock crushes Lizard!')
                     print(f'\n{ai_1.name} Wins!!')
               
                  #Paper vs Scissors or Spock
            elif ai_1.move_list[ai_choice] == ai_1.move_list[1]:
               if choice1 == human_1.move_list[2] or choice1 == human_1.move_list[4]:
                  ai_1.wins +=1
                  if choice1 == human_1.move_list[2]:
                     print('\nScissors cuts Paper!\n')
                     print(f'\n{ai_1.name} Wins!!')
                  elif choice1 == human_1.move_list[4]:
                     print('\nPaper disproves Spock\n')
                     print(f'\n{ai_1.name} Wins!!')
               
                  #Scissors vs Paper or Lizard
            elif ai_1.move_list[ai_choice] == ai_1.move_list[2]:
               if choice1 == human_1.move_list[1] or choice1 == human_1.move_list[3]:
                  ai_1.wins +=1
                  if choice1 == human_1.move_list[1]:
                     print('\nScissors cuts Paper\n')
                     print(f'\n{ai_1.name} Wins!!')
                  elif choice1 == human_1.move_list[3]:
                     print('\nScissors decapitates Lizard\n')
                     print(f'\n{ai_1.name} Wins!!')
                  
                  #Lizard vs Spock or Paper
            elif ai_1.move_list[ai_choice] == ai_1.move_list[3]:

               if choice1 == human_1.move_list[4] or choice1 == human_1.move_list[1]:
                  ai_1.wins +=1
                  if choice1 == human_1.move_list[4]:
                     print('\nLizard poisons Spock\n')
                     print(f'\n{ai_1.name} Wins!!')
                  elif choice1 == human_1.move_list[1]:
                     print('\nLizard eats Paper\n')
                     print(f'\n{ai_1.name} Wins!!')
            
                  #Spock vs Scissors or Rock
            elif ai_1.move_list[ai_choice] == ai_1.move_list[4]:
               if choice1 == human_1.move_list[2] or choice1 == human_1.move_list[0]:
                  ai_1.wins +=1
                  if choice1 == human_1.move_list[2]:
                     print('\nSpock smashes Scissors\n')
                     print(f'\n{ai_1.name} Wins!!')
                  elif choice1 == human_1.move_list[0]:
                     print('\nSpock vaporizes Rock\n')
                     print(f'\n{ai_1.name} Wins!!')

         ## Human Wins

                  #Rock vs either Scissors or Lizard
            if choice1 == human_1.move_list[0]:
               if ai_1.move_list[ai_choice] == ai_1.move_list[2] or choice1 == ai_1.move_list[3]:
                  human_1.wins +=1
                  if ai_1.move_list[ai_choice] == ai_1.move_list[2]:
                     print('\nRock crushes Scissors!\n')
                     print(f'\n{human_1.name} Wins!!')
                  elif choice1 == ai_1.move_list[3]:
                     print('\n Rock crushes Lizard!')
                     print(f'\n{human_1.name} Wins!!')

                     
                  #Paper vs Rock or Spock
            elif choice1 == human_1.move_list[1]:
               if ai_1.move_list[ai_choice] == ai_1.move_list[0] or choice1 == ai_1.move_list[4]:
                  human_1.wins +=1
                  if ai_1.move_list[ai_choice] == ai_1.move_list[2]:
                     print('\nPaper covers Rock!\n')
                     print(f'\n{human_1.name} Wins!!')
                  elif choice1 == ai_1.move_list[4]:
                     print('\nPaper disproves Spock\n')
                     print(f'\n{human_1.name} Wins!!')
                  
                  #Scissors vs Paper or Lizard
            elif choice1 == human_1.move_list[2]:
               if ai_1.move_list[ai_choice] == ai_1.move_list[1] or choice1 == ai_1.move_list[3]:
                  human_1.wins +=1
                  if ai_1.move_list[ai_choice] == ai_1.move_list[1]:
                     print('\nScissors cuts Paper!\n')
                     print(f'\n{human_1.name} Wins!!')
                  elif choice1 == ai_1.move_list[3]:
                     print('\nScissors decapitates Lizard\n')
                     print(f'\n{human_1.name} Wins!!')

                  
                  #Lizard vs Spock or Paper
            elif choice1 == human_1.move_list[3]:
               if ai_1.move_list[ai_choice] == ai_1.move_list[4] or choice1 == ai_1.move_list[1]:
                  human_1.wins +=1
                  if ai_1.move_list[ai_choice] == ai_1.move_list[4]:
                     print('\nLizard poisons Spock\n')
                     print(f'\n{human_1.name} Wins!!')
                  elif choice1 == ai_1.move_list[1]:
                     print('\nLizard eats Paper\n')
                     print(f'\n{human_1.name} Wins!!')

                  
                  #Spock vs Scissors or Rock
            elif choice1 == human_1.move_list[4]:
               if ai_1.move_list[ai_choice] == ai_1.move_list[2] or choice1 == ai_1.move_list[0]:
                  human_1.wins +=1
                  if ai_1.move_list[ai_choice] == ai_1.move_list[2]:
                     print('\nSpock smashes Scissors\n')
                     print(f'\n{human_1.name} Wins!!')
                  elif choice1 == ai_1.move_list[0]:
                     print('\nSpock vaporizes Rock\n')
                     print(f'\n{human_1.name} Wins!!')
                     
         
            else:
               print("I'm sorry, I didn't understand that message!")
      

         winner = ''
         if human_1.wins >= 2:
            winner = human_1.name
         else:
            winner = ai_1.name

         return winner
      

   def win_game(self, winner):
      print(f"Congratulations to {winner}!")
      playsound('./for_final_win.wav')
      # sleep(1)
      answer = input("Would you like to play again? (y/n)")
      return answer