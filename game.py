
from human import Human 
from ai import AI
from player import Player
from time import sleep

human_1 = Human()
human_2 = Human()
human_1.name = "Player 1"
human_2.name = "Player 2"
ai_1 = AI()
ai_1.name = "Computer"
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
      winner = self.play_game(player_number)
      answer = self.win_game(winner)
      answer = ""
      while answer == "y":
         winner = self.play_game(player_number)
         answer = self.win_game(winner)
      print("Thanks for playing!")



   def display_welcome(self):
    print('\nWelcome to Rock Paper Scissors Spock!\n')
    sleep(1)
    number_of_players = input('''\n
    How many players would you like to have? (single/multi). 
    We're playing best out of three, so first to two wins!\n''')
    sleep(1)
    print(f"{self.rules}")
    sleep(1)
    return number_of_players



   def play_game(self, number_of_players):
      
      if number_of_players == "multi":
         while human_1.wins < 2 or human_2.wins < 2:              


            choice = human_1.make_choice()
            print(f'''{human_2.name} - no peeking!









            ''')
            choice1 = human_2.make_choice()

            if choice == choice1:
               print("It's a tie!")
            
            elif choice == human_1.move_list[0]:
                  if choice1 == human_2.move_list[2] or choice1 == human_2.move_list[3]:
                     human_1.wins += 1
                  
            elif choice == human_1.move_list[1]:
                  if choice1 == human_2.move_list[2] or choice1 == human_2.move_list[4]:
                     human_1.wins += 1
               
            elif choice == human_1.move_list[2]:
                  if choice1 == human_2.move_list[1] or choice1 == human_2.move_list[3]:
                     human_1.wins += 1
            
            elif choice == human_1.move_list[3]:
                  if choice1 == human_2.move_list[4] or choice1 == human_2.move_list[2]:
                     human_1.wins += 1
            
            elif choice == human_1.move_list[4]:
                  if choice1 == human_2.move_list[2] or choice1 == human_2.move_list[0]:
                     human_1.wins += 1

            
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
               
            # self.move_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

                  #Rock vs either Scissors or Lizard
            elif ai_1.move_list[ai_choice] == ai_1.move_list[0]:
                  if choice1 == human_1.move_list[2] or choice1 == human_1.move_list[3]:
                     ai_1.wins +=1
                  
                  #Paper vs Scissors or Spock
            elif ai_1.move_list[ai_choice] == ai_1.move_list[1]:
                  if choice1 == human_1.move_list[2] or choice1 == human_1.move_list[4]:
                     ai_1.wins +=1
               
                  #Scissors vs Paper or Lizard
            elif ai_1.move_list[ai_choice] == ai_1.move_list[2]:
                  if choice1 == human_1.move_list[1] or choice1 == human_1.move_list[3]:
                     ai_1.wins +=1
            
                  #Lizard vs Spock or Scissors
            elif ai_1.move_list[ai_choice] == ai_1.move_list[3]:
                  if choice1 == human_1.move_list[4] or choice1 == human_1.move_list[2]:
                     ai_1.wins +=1
            
                  #Spock vs Scissors or Rock
            elif ai_1.move_list[ai_choice] == ai_1.move_list[4]:
                  if choice1 == human_1.move_list[2] or choice1 == human_1.move_list[0]:
                     ai_1.wins +=1



                  #Rock vs either Scissors or Lizard
            if choice1 == human_1.move_list[0]:
                  if ai_1.move_list[ai_choice] == ai_1.move_list[2] or choice1 == ai_1.move_list[3]:
                     human_1.wins                       
                     
                  #Paper vs Scissors or Spock
            elif choice1 == human_1.move_list[1]:
                  if ai_1.move_list[ai_choice] == ai_1.move_list[2] or choice1 == ai_1.move_list[4]:
                     human_1.wins +=1
                  
                  #Scissors vs Paper or Lizard
            elif choice1 == human_1.move_list[2]:
                  if ai_1.move_list[ai_choice] == ai_1.move_list[1] or choice1 == ai_1.move_list[3]:
                     human_1.wins +=1
                  
                  #Lizard vs Spock or Scissors
            elif choice1 == human_1.move_list[3]:
                  if ai_1.move_list[ai_choice] == ai_1.move_list[4] or choice1 == ai_1.move_list[2]:
                     human_1.wins +=1
                  
                  #Spock vs Scissors or Rock
            elif choice1 == human_1.move_list[4]:
                  if ai_1.move_list[ai_choice] == ai_1.move_list[2] or choice1 == ai_1.move_list[0]:
                     human_1.wins +=1
         
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
      sleep(1)
      answer = input("Would you like to play again? (y/n)")
      return answer