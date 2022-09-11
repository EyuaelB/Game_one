
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
    # def play_game(self,game):
    #     game= game(self)
    #     game.start()

