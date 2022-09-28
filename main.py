import os
import random
import time
import utility
from user import User
from game import Game


def main():

    utility.display_clear_normal("Welcome, \n")
    name = input("Enter Your Name To Play The Game... \n")

    player = User(name)
    game = Game(player)

    print("\n")
    time.sleep(2)
    utility.display_clear_prog_str("Hello")
    # Game.start()
    utility.display_clear(
        "I will iterate and randomly select a number from Zero and One, and you Have to Guess"
    )

    while True:
        rand_num = random.randint(0, 2)
        num = int(input("Enter Your guess \n"))
        game.game_prompt(player, num, rand_num)

        if player.pts == 50:
            print("Congratulations you have reached 50pts")
            break


if __name__ == "__main__":
    main()
