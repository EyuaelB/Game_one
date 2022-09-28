import time


def prog_str_for_print(some_str: str) -> None:
    for x in range(0, 4):
        b = some_str + "." * x
        print(b, end="\r")
        time.sleep(1)


def display_clear(some_str: str) -> None:
    # print('I will iterate and randomly select a number from Zero to Ten including Zero and Ten you Have to Guess \n')
    print(some_str + "\n")
    # os.system('clear')
    time.sleep(2)


def display_clear_prog_str(some_str: str) -> None:
    prog_str_for_print(some_str)
    # os.system('clear')
    time.sleep(2)


def display_clear_normal(some_str: str) -> None:
    print(some_str)
    # os.system('clear')
    time.sleep(2)
