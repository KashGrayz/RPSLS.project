#Player (parent class)

class Player:

    def __init__(self):
        self.name = ''
        self.wins = 0
        self.moves_list = []
        #list to display before each play
        self.moves_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

        #determines winner of each round
    def make_choice(self):
        
        choice = input(f"{self.name}, please choose a weapon.")
        choice1 = input(f"{self.name}, please choose a weapon.")
        
        winner = 0
        #winner_p2 = 0

        if choice == self.move_list[0]:
            if choice1 == self.move_list[2] or choice1 == self.move_list[3]:
                winner+=1
            
        elif choice == self.move_list[1]:
            if choice1 == self.move_list[2] or choice1 == self.move_list[4]:
                winner+= 1
           
        elif choice == self.move_list[2]:
            if choice1 == self.move_list[1] or choice1 == self.move_list[3]:
                winner+=1
        
        elif choice == self.move_list[3]:
            if choice1 == self.move_list[4] or choice1 == self.move_list[2]:
                winner+= 1
        
        elif choice == self.move_list[4]:
            if choice1 == self.move_list[2] or choice1 == self.move_list[0]:
                winner+=1


        
        # if choice1 == self.move_list[0]:
        #     if choice == self.move_list[2] or choice1 == self.move_list[3]:
        #         winner_p2 +=1
            
        # elif choice1 == self.move_list[1]:
        #     if choice == self.move_list[2] or choice1 == self.move_list[4]:
        #         winner_p2 +=1
           
        # elif choice1 == self.move_list[2]:
        #     if choice == self.move_list[1] or choice1 == self.move_list[3]:
        #         winner_p2 +=1
        
        # elif choice1 == self.move_list[3]:
        #     if choice == self.move_list[4] or choice1 == self.move_list[2]:
        #         winner_p2 +=1
        
        # elif choice1 == self.move_list[4]:
        #     if choice == self.move_list[2] or choice1 == self.move_list[0]:
        #         winner_p2 +=1
        
        
        else:
            print("I'm sorry, I didn't understand that message!")
        
        #return winner, winner_p2