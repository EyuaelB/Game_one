import os
import random  
import time
import utility
from user import User
from game import Game



def main():

    utility.display_clear_normal('Welcome, \n')
    name = input('Enter Your Name To Play The Game... \n')

    player = User(name)
    game = Game(player)
                
    # usr.play_game(game)

    # game.start()
    print('\n')
    time.sleep(2)
    utility.display_clear_prog_str('Hello')
    utility.display_clear('I will iterate and randomly select a number from Zero to Ten including Zero and Ten you Have to Guess')


# def prompt(player,game,num:int)->None:
#     while True:
#         if(usr.pts is not None and usr.pts < 50):
#             rand_num = random.randint(0,10)
#             # num = input('Enter Your guess \n')
#             game.check_usr_input_num(num,rand_num)

#         else:
#             utility.display_clear_prog_str('Congrattulations')
#             utility.display_clear_normal('your point have reache 50')
#             print('Conne:
    while True:
        rand_num = random.randint(0,10)
        num = int(input('Enter Your guess \n'))
        game.game_prompt(player,num,rand_num)

        if(player.pts==50):
            print('Congratulations you have reached 50pts')
            break

 


if __name__=='__main__':
    main()
