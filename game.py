from user import User
import os
import time
import utility
import enum


class Game:
    class Game_status(enum.Enum):
        """_summary_

        Args:
            enum (int): Determines status of a Game, Win, Lose or In progress
            (unfinished).
        """

        LOSE = (0,)
        WIN = (1,)
        Default = None

    player: User
    GAME_COST = 10
    status: int

    def __init__(self, User: User) -> None:
        self.player = User
        self.status = self.Game_status.Default

    # usr_input_num=int(input('Guess a number between 0 and 10'))

    def apply_game_cost(self) -> None:
        if self.status == 1:
            self.player.award(10)
            self.status = None
        else:
            self.player.penality(10)
            self.status = None
            
    # @classmethod
    # def start() -> None:
    #     utility.display_clear_prog_str("\n Hello")
    #     utility.display_clear(
    #         "\n I will iterate and randomly select a number from Zero and one with game cost of 10pts , you Have to Guess"
    #     )

    def chk_pt(self) -> str:
        if self.status != None:
            return str(self.player.pts)
        else:
            return "the game must not be in progress"

    def check_usr_input_num(self, usr_num: int, comp_gen: int) -> None:

        if usr_num == comp_gen:
            self.status = 1
            self.apply_game_cost()
            print(
                f"Great, you've enterd the right number you are awrarded 10pts , your point is now {self.player.pts}"
            )
        elif usr_num is None:
            print("please enter a valid number")
        else:
            self.status = 0
            self.apply_game_cost()
            print(
                f"Wrong, Try A gain,  the number was {comp_gen}, penality: -10p, your point is now {self.player.pts}"
            )

    def game_prompt(self, player: User, num: int, comp_gen: int) -> None:

        if player.pts is not None and player.pts < 50:
            self.check_usr_input_num(num, comp_gen)

        else:
            utility.display_clear_prog_str("Congrattulations")
            utility.display_clear_normal("your point have reache 50")
            print("Consider updating Level?")
