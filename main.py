import enum
from random import random
from time import thread_time, time
from typing_extensions import Self
rand_num = random.randint(0,10)


class User():
    usr_name: str
    pts : int

    def __init__(self,usr_name):
       self.usr_name =usr_name
       self.pts = 0 

    def award(self,n:int):
        self.pts = self.pts+n
        
    def penality(self,n:int):
        self.pts = self.pts-n
    
    def chk_pts_against_50(self):
        if self.pts<50:
            return f"The user has only {self.pts}"
        else:
            return "user already reached 50pts" 
        # elif(self.pts>50):
        #     return 'User already has more '
        # else:
        #     return "Congratulation you have Scored the highest point. You are Legend"
    def play_game(self):
        game= Game(self)
        game.start()


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           


# abebe = User('ab')


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


    def start():
        

    
    def check_usr_input_num(self,usr_num:int,comp_gen:int):

        if(usr_num == comp_gen):
            print("Great, you've enterd the right number you are awrarded 10pts")
            self.status= 1
        elif (usr_num is None):
            print("please enter a valid number")
        else:
            print("Wrong, Try A gain, -10p")
            self.status = 0

    def apply_game_cost(self,):
        if(self.status==1):
            self.award(Game.GAME_COST)
        else:
            self.penality(Game.GAME_COST)








# "Hello Welcome to the game"