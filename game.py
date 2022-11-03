
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
      answer = ""
      while answer == "y":
         winner = self.play_game(player_number)
         answer = self.win_game(winner)
      print("\nThanks for playing!\n")


   def display_welcome(self):
      playsound('./winbrass.wav')

      print('\nWelcome to Rock Paper Scissors Spock!\n')
      sleep(1)
      number_of_players = input('''
      \nHow many players would you like to have? (single/multi). 
      We're playing best out of three, so first to two wins!\n''')
      sleep(1)
      print(f"{self.rules}")
      sleep(1)
      return number_of_players


   def play_game(self, number_of_players):
      
      if number_of_players == "multi":
         while human_1.wins < 2 or human_2.wins < 2:              


            choice = human_1.make_choice()
            print(f'''\n{human_2.name} - no peeking!\n









            ''')
            choice1 = human_2.make_choice()

            if choice == choice1:
               print("It's a tie!")

            ## Human 1 Wins

                  #Rock vs either Scissors or Lizard
            elif choice == human_1.move_list[0]:
                  if choice1 == human_2.move_list[2] or choice1 == human_2.move_list[3]:
                     human_1.wins += 1
                    # if choice1 == human_2.move_list[2]:
                    
                  #Paper vs Scissors or Spock     
            elif choice == human_1.move_list[1]:
                  if choice1 == human_2.move_list[2] or choice1 == human_2.move_list[4]:
                     human_1.wins += 1
                  #Paper vs Scissors or Spock
            elif choice == human_1.move_list[2]:
                  if choice1 == human_2.move_list[1] or choice1 == human_2.move_list[3]:
                     human_1.wins += 1
                  #Lizard vs Spock or Scissors
            elif choice == human_1.move_list[3]:
                  if choice1 == human_2.move_list[4] or choice1 == human_2.move_list[2]:
                     human_1.wins += 1
                   #Spock vs Scissors or Rock
            elif choice == human_1.move_list[4]:
                  if choice1 == human_2.move_list[2] or choice1 == human_2.move_list[0]:
                     human_1.wins += 1

            ## Human 2 Wins

                     #Rock vs either Scissors or Lizard
            if choice1 == human_2.move_list[0]:
                  if choice == human_1.move_list[2] or choice1 == human_1.move_list[3]:
                     human_2.wins += 1
                  
            elif choice1 == human_2.move_list[1]:
                  if choice == human_1.move_list[2] or choice1 == human_1.move_list[4]:
                     human_2.wins += 1
               
            elif choice1 == human_2.move_list[2]:
                  if choice == human_1.move_list[1] or choice1 == human_1.move_list[3]:
                     human_2.wins += 1
            
            elif choice1 == human_2.move_list[3]:
                  if choice == human_1.move_list[4] or choice1 == human_1.move_list[2]:
                     human_2.wins += 1
            
            elif choice1 == human_2.move_list[4]:
                  if choice == human_1.move_list[2] or choice1 == human_1.move_list[0]:
                     human_2.wins += 1
            
            
            else:
               print("I'm sorry, I didn't understand that message!")
        
         winner = ''
         if human_1.wins < 2:
            winner = human_1.name
         else:
            winner = ai_1.name

         return winner

         
      elif number_of_players == "single":
         while human_1.wins or ai_1.wins < 2:
         
            choice1 = human_1.make_choice()
            ai_choice = ai_1.make_choice()
            
            if ai_1.move_list[ai_choice] == choice1:
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
                  
            
                  #Lizard vs Spock or Scissors
            elif ai_1.move_list[ai_choice] == ai_1.move_list[3]:
                  if choice1 == human_1.move_list[4] or choice1 == human_1.move_list[2]:
                     ai_1.wins +=1
                     if choice1 == human_1.move_list[4]:
                        print('\nLizard poisons Spock\n')
                        print(f'\n{ai_1.name} Wins!!')
                     elif choice1 == human_1.move_list[2]:
                        print('\nScissors decapitates Lizard\n')
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

                     
                  #Paper vs Scissors or Spock
            elif choice1 == human_1.move_list[1]:
                  if ai_1.move_list[ai_choice] == ai_1.move_list[2] or choice1 == ai_1.move_list[4]:
                     human_1.wins +=1
                     if ai_1.move_list[ai_choice] == ai_1.move_list[2]:
                        print('\nScissors cuts Paper!\n')
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

                  
                  #Lizard vs Spock or Scissors
            elif choice1 == human_1.move_list[3]:
                  if ai_1.move_list[ai_choice] == ai_1.move_list[4] or choice1 == ai_1.move_list[2]:
                     human_1.wins +=1
                     if ai_1.move_list[ai_choice] == ai_1.move_list[4]:
                        print('\nLizard poisons Spock\n')
                        print(f'\n{human_1.name} Wins!!')
                     elif choice1 == ai_1.move_list[2]:
                        print('\nScissors decapitates Lizard\n')
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
      playsound('./winbrass.wav')
      print(f"Congratulations to {winner}!")
      sleep(1)
      answer = input("Would you like to play again? (y/n)")
      return answer