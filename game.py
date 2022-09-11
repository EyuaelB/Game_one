from user import User
import os
import time
import utility
import enum


class Game():
    class Game_status(enum.Enum):
        LOSE=0
        WIN =1
        Default = None
        
    player: User
    GAME_COST=10
    status: int
 
      

    def __init__(self,User) -> None:
        self.player = User
        status = self.Game_status.Default
    
    
    
    
    # usr_input_num=int(input('Guess a number between 0 and 10'))

    # def 
    def apply_game_cost(self):
        if(self.status==1):
            self.player.award(10)
        else:
            self.player.penality(10)

    def start():
        utility.display_clear_prog_str('Hello')
        utility.display_clear('I will iterate and randomly select a number from Zero to Ten including Zero and Ten you Have to Guess')


    def chk_pt(self):
        if(self.status!=None):
            return str(self.player.pts)
        else:
            return 'the game must not be in progress'


    def check_usr_input_num(self,usr_num:int,comp_gen:int):

        if(usr_num == comp_gen):
            print("Great, you've enterd the right number you are awrarded 10pts")
            self.status= 1
            self.apply_game_cost()
        elif (usr_num is None):
            print("please enter a valid number")
        else:
            print(f"Wrong, Try A gain,  the number was {comp_gen},-10p, {self.player.pts}")
            self.status = 0
            self.apply_game_cost()

    
   
   


