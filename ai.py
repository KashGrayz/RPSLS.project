#AI(child class)

import random
from player import Player

class AI(Player):

    def __init__(self):

        super().__init__()
        
    def make_choice(self):
        ai_choice = random.randint(0, 4)
        choice1 = input(f"{self.name}, please choose a weapon.")

        winner = 0
        winner_p2 = 0

        if self.move_list[ai_choice] == self.move_list[0]:
            if choice1 == self.move_list[2] or choice1 == self.move_list[3]:
                winner+=1
            
        elif self.move_list[ai_choice] == self.move_list[1]:
            if choice1 == self.move_list[2] or choice1 == self.move_list[4]:
                winner+= 1
           
        elif self.move_list[ai_choice] == self.move_list[2]:
            if choice1 == self.move_list[1] or choice1 == self.move_list[3]:
                winner+=1
        
        elif self.move_list[ai_choice] == self.move_list[3]:
            if choice1 == self.move_list[4] or choice1 == self.move_list[2]:
                winner+= 1
        
        elif self.move_list[ai_choice] == self.move_list[4]:
            if choice1 == self.move_list[2] or choice1 == self.move_list[0]:
                winner+=1


        
        if choice1 == self.move_list[0]:
            if self.move_list[ai_choice] == self.move_list[2] or choice1 == self.move_list[3]:
                winner_p2 +=1
            
        elif choice1 == self.move_list[1]:
            if self.move_list[ai_choice] == self.move_list[2] or choice1 == self.move_list[4]:
                winner_p2 +=1
           
        elif choice1 == self.move_list[2]:
            if self.move_list[ai_choice] == self.move_list[1] or choice1 == self.move_list[3]:
                winner_p2 +=1
        
        elif choice1 == self.move_list[3]:
            if self.move_list[ai_choice] == self.move_list[4] or choice1 == self.move_list[2]:
                winner_p2 +=1
        
        elif choice1 == self.move_list[4]:
            if self.move_list[ai_choice] == self.move_list[2] or choice1 == self.move_list[0]:
                winner_p2 +=1
    
        else:
            print("I'm sorry, I didn't understand that message!")