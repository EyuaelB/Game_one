import os
import random  
import time
import utility
from user import User
from game import Game



def main():

    utility.display_clear_normal('Welcome, \n')
    name = input('Enter Your Name To Play The Game \n')

    usr = User(name)
    game = Game(usr)

    # usr.play_game(game)
    # game.start()

    while True:
        if(usr.pts is not None and usr.pts < 50):
            rand_num = random.randint(0,10)
            num = input('Enter Your guess \n')
            game.check_usr_input_num(num,rand_num)

        else:
            utility.display_clear_prog_str('Congrattulations')
            utility.display_clear_normal('your point have reache 50')
            print('Consiider updating Level?')
            break

    # print(str(5-10))


if __name__=='__main__':
    main()
