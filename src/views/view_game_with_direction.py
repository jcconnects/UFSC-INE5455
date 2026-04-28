from exercicio_3_src.src import PuzzleGame
from exercicio_3_src.src import ShufflePuzzleLevelEasy, ShufflePuzzleLevelMedium, \
    ShufflePuzzleLevelHard

def play_game_using_directions_for_empty_tile():
    puzzle_game = PuzzleGame(3)
    entry = input("Enter the difficulty of the level game (1-easy 2-medium 3-hard): ")
    if (entry == "1"):
        ShufflePuzzleLevelEasy().shuffle(puzzle_game)
    elif (entry == "2"):
        ShufflePuzzleLevelMedium().shuffle(puzzle_game)
    elif (entry == "3"):
        ShufflePuzzleLevelHard().shuffle(puzzle_game)
    else:
        return
    puzzle_game.__print_board_of_puzzle_game__()
    while not puzzle_game.end_of_the_game() and not entry == "end":
        entry = input("Enter the letter of the direction (w-up a-left s-down d-right) or \"end\" to terminate the game: ")
        if entry == "w":
            puzzle_game.move_empty_tile("UP")
        elif entry == "a":
            puzzle_game.move_empty_tile("LEFT")
        elif entry == "s":
            puzzle_game.move_empty_tile("DOWN")
        elif entry == "d":
            puzzle_game.move_empty_tile("RIGHT")
        puzzle_game.__print_board_of_puzzle_game__()
    print("The End.")

play_game_using_directions_for_empty_tile()